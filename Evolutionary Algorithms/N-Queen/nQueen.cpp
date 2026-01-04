#include <iostream>
#include <bits/stdc++.h>
#include <fstream>

using namespace std;


int n = 8, q = 8, fundNum = 12, populationNum = 30;
int printX = 3, printY = 4;
double elitismRate = 0, mutationRate = 0.8;
random_device rd;
mt19937 gen(rd());
uniform_int_distribution<> ran0toQ(0, q - 1);
uniform_int_distribution<> ran0toN(0, n - 1);
uniform_int_distribution<> ran0toPopSize(0, populationNum - 1);
uniform_real_distribution<> ran0to1(0.0, 1.0);


struct chromosome {
    int fitness = 0;
    vector<pair<int, int>> coordinate;
};

vector<chromosome> population;
vector<vector<pair<int, int>>> allValids;
vector<vector<pair<int, int>>> fundamentals;
vector<vector<vector<char>>> strFund;

bool cmp(chromosome a, chromosome b) {
    return a.fitness < b.fitness;
}


int fitnessCalculator(vector<pair<int, int>> coordinates) {
    int fit = 0;
    for (int i = 0; i < coordinates.size(); i++) {
        for (int j = i + 1; j < coordinates.size(); ++j)
            if (abs(coordinates[i].first - coordinates[j].first) ==
                abs(coordinates[i].second - coordinates[j].second) || coordinates[i].first == coordinates[j].first ||
                coordinates[i].second == coordinates[j].second) {
                fit++;
            }
    }

    return fit;
}

void initPopulation(int initNum) {
    int x, y;
    for (int i = 0; i < initNum; ++i) {
        chromosome state;
        for (int j = 0; j < q; ++j) {
            x = ran0toN(gen);
            y = j;
            state.coordinate.push_back(make_pair(x, y));
        }
        state.fitness = fitnessCalculator(state.coordinate);
        population.push_back(state);
    }
}


chromosome offspring(vector<pair<int, int>> pX, vector<pair<int, int>> pY) {
    chromosome offspring;
    vector<bool> filled(n);
    int r;
    for (int i = 0; i < q / 2;) {
        do {
            r = ran0toQ(gen);
        } while (filled[pX[r].second]);
        i++;
        offspring.coordinate.push_back(pX[r]);
        filled[pX[r].second] = true;
    }
    for (int i = 0; i < (q - q / 2);) {
        do {
            r = ran0toQ(gen);
        } while (filled[pY[r].second]);
        i++;
        offspring.coordinate.push_back(pY[r]);
        filled[pY[r].second] = true;
    }
    offspring.fitness = fitnessCalculator(offspring.coordinate);
    return offspring;
}

void Elitism(vector<chromosome> &nG) {
    for (int i = 0; i < elitismRate; ++i) {
        nG.push_back(population[i]);
    }
}

int chooseParent(set<int> &idxList) {
    int k = 5, idx;
    vector<pair<int, int>> candidates;
    for (int i = 0; i < k; ++i) {
        do {
            idx = ran0toPopSize(gen);
        } while (idxList.find(idx) != idxList.end());
        idxList.insert(idx);
        candidates.push_back(make_pair(population[idx].fitness, idx));
    }
    sort(candidates.begin(), candidates.end());
    return candidates[0].second;
}

vector<chromosome> crossover() {
    vector<chromosome> newGen;
    chromosome OS1, OS2;
    int pX, pY;
    while (newGen.size() < populationNum - elitismRate) {
        set<int> chosen;
        pX = chooseParent(chosen);
        pY = chooseParent(chosen);
        OS1 = offspring(population[pX].coordinate, population[pY].coordinate);
        newGen.push_back(OS1);
        OS2 = offspring(population[pY].coordinate, population[pX].coordinate);
        newGen.push_back(OS2);
    }
    return newGen;
}

int mutated = 0;

void Mutation(vector<chromosome> &newGen) {
    double r;
    int x, newX, gene;
    for (int i = 0; i < newGen.size(); ++i) {
        r = ran0to1(gen);
        if (r <= mutationRate) {
            mutated++;
            gene = ran0toQ(gen);
            x = newGen[i].coordinate[gene].first;
            do {
                newX = ran0toN(gen);
            } while (x == newX);
            newGen[i].coordinate[gene].first = newX;
            newGen[i].fitness = fitnessCalculator(newGen[i].coordinate);
        }
    }
}


void newDetected(vector<pair<int, int>> board) {
    sort(board.begin(), board.end());
    fundamentals.push_back(board);
    allValids.push_back(board);
    vector<pair<int, int>> rotate(q);
    vector<pair<int, int>> reflect(q);
    int tmp;
    rotate = board;
    for (int j = 0; j < 3; ++j) {
        for (int i = 0; i < q; ++i) {
            tmp = rotate[i].first;
            rotate[i].first = rotate[i].second;
            rotate[i].second = n - tmp - 1;
        }
        sort(rotate.begin(), rotate.end());
        allValids.push_back(rotate);
        for (int i = 0; i < q; ++i) {
            reflect[i].first = n - rotate[i].first - 1;
            reflect[i].second = rotate[i].second;
        }
        sort(reflect.begin(), reflect.end());
        allValids.push_back(reflect);
    }
    for (int i = 0; i < q; ++i) {
        reflect[i].first = n - board[i].first - 1;
        reflect[i].second = board[i].second;
    }
    sort(reflect.begin(), reflect.end());
    allValids.push_back(reflect);
}

bool checkRepeated(vector<pair<int, int>> coor) {
    bool diff, noRep = true;
    sort(coor.begin(), coor.end());
    vector<pair<int, int>> inst;
    for (int i = 0; i < allValids.size(); ++i) {
        diff = false;
        inst = allValids[i];
        for (int j = 0; j < q; ++j) {
            if (inst[j].first != coor[j].first || inst[j].second != coor[j].second)
                diff = true;
        }
        noRep &= diff;
    }
    if (noRep) {
        newDetected(coor);
        return true;
    }
    return false;
}

vector<vector<char>> print(vector<pair<int, int>> p) {
    vector<vector<char>> print(n, vector<char>(n));
    for (int i = 0; i < q; ++i) {
        print[p[i].first][p[i].second] = 'Q';
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (print[i][j] != 'Q')
                print[i][j] = '.';
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << print[i][j] << "  ";
        }
        cout << endl;
    }
    return print;
}

void save(double t) {
    vector<string> s;
    for (int i = 0; i < printX; ++i) {
        s.push_back(
                "  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ");
        for (int r = 0; r < n; ++r) {
            string row = "|   ";
            for (int j = 0; j < printY; ++j) {
                if (printY * i + j >= fundNum) break;
                for (int c = 0; c < n; ++c) {
                    row += strFund[printY * i + j][r][c];
                    row += "  ";
                }
                row += " |  ";
            }
            s.push_back(row);
        }
    }
    s.push_back(
            "  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ");
    fstream file("..\\Results.txt", ::ios_base::app);
    file << "\n\n" << "Results: (q = " << q << ") in " << t << " secs" << endl;
    file << "Population Number: " << populationNum << ",  " << "Mutation Rate: " << mutationRate << ",  "
         << "Elitism Rate: " << elitismRate << endl;
    for (int i = 0; i < s.size(); ++i) {
        file << (s[i] + "\n");
    }
    file.close();
}

void giveStatus(int s) {
    cout << "Generation: " << s << endl;
    cout << "People Fitness: ";
    for (int i = 0; i < population.size(); ++i) {
        cout << population[i].fitness << ", ";
    }
    cout << endl;
    cout
            << "-------------------------------------------------------------------------------------------------------------"
            << endl;
    for (int i = 0; i < fundamentals.size(); ++i) {
        cout << i << ": " << endl;
        print(fundamentals[i]);
        cout << "^^^^^^^^^^^^^^^^^^^^^^^" << endl;
    }
}

int main() {
    clock_t b = clock();
    initPopulation(populationNum);
    int Step = 0;
    while (true) {
        Step++;
        if (population[0].fitness == 0) {
            while (population[0].fitness == 0) {
                checkRepeated(population[0].coordinate);
                population.erase(population.begin());
            }
            population.clear();
            initPopulation(populationNum);
        }
        vector<chromosome> newGEN = crossover();
        Mutation(newGEN);
        Elitism(newGEN);
        population.clear();
        population = newGEN;
        sort(population.begin(), population.end(), cmp);
        if (Step % 500 == 0) {
            giveStatus(Step);
        }
        if (fundamentals.size() >= fundNum) break;
    }
    for (int i = 0; i < fundamentals.size(); ++i) {
        cout << i << ": " << endl;
        strFund.push_back(print(fundamentals[i]));
        cout << "^^^^^^^^^^^^^^^^^^^^^^^" << endl;
    }
    double time = (double) (clock() - b) / CLOCKS_PER_SEC;
    save(time);
    cout << time << " Secs";
    return 0;
}
