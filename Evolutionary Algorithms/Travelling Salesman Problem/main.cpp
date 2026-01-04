#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int populationSize = 80, elitismRate = 1;
double mutationRate = 0.8;
random_device rd;
mt19937 gen(rd());
uniform_real_distribution<> ran0to1(0.0, 1.0);
uniform_int_distribution<> ran0to50(0, 50);
uniform_int_distribution<> ran0toPopSize(0, populationSize - 1);


int cityNum = 51;
vector<vector<double>> adj(cityNum + 1, vector<double>(cityNum + 1, 0));
vector<vector<int>> Locations;
vector<int> possibleNodes(cityNum);
struct path {
    double fitness = 0;

    vector<int> route;
};
vector<path> population;

void readInfo(string address) {
    ifstream file(address);
    string line;
    if (!file.is_open()) {
        cerr << "Error opening file." << endl;
    }
    while (getline(file, line)) {
        stringstream ss(line);
        string value;
        vector<int> row;
        while (getline(ss, value, ' ')) {
            row.push_back(stoi(value));
        }
        Locations.push_back({row[0], row[1], row[2]});
    }
    file.close();
}

bool cmp(path a, path b) {
    return a.fitness < b.fitness;
}


void distanceCalculator() {
    double d;
    int l1, l2, x1, x2, y1, y2;
    // Permutation of all location pairs
    for (int i = 0; i < Locations.size(); i++) {
        for (int j = i; j < Locations.size(); j++) {
            l1 = (Locations[i][0]);
            x1 = (Locations[i][1]);
            y1 = (Locations[i][2]);
            l2 = (Locations[j][0]);
            x2 = (Locations[j][1]);
            y2 = (Locations[j][2]);
            d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
            adj[l1][l2] = d;
            adj[l2][l1] = d;
        }
    }
}

double fitnessCalculator(vector<int> route) {
    double fit = 0;
    int a, b;
    for (int i = 0; i < cityNum - 1; i++) {
        a = route[i];
        b = route[i + 1];
        fit += adj[a][b];
    }
    fit += adj[route[route.size() - 1]][route[0]];
    return fit;
}


void initPath(int initNum) {
    for (int i = 0; i < initNum; ++i) {
        path chromosome;
        shuffle(possibleNodes.begin(), possibleNodes.end(), gen);
        chromosome.route = (possibleNodes);
        chromosome.fitness = fitnessCalculator(chromosome.route);
        population.push_back(chromosome);
    }
}

path offspring(vector<int> pX, vector<int> pY, int sbound, int ebound) {
    path OS;
    vector<bool> used(cityNum + 1);
    OS.route.resize(cityNum, -1);
    for (int i = sbound; i <= ebound; ++i) {
        OS.route[i] = pX[i];
        used[pX[i]] = true;
    }
    int j = 0;
    for (int i = 0; i < cityNum; ++i) {
        if (i >= sbound && i <= ebound) continue;
        while (used[pY[j]]) j++;
        OS.route[i] = pY[j];
        j++;
    }
    OS.fitness = fitnessCalculator(OS.route);
    return OS;
}

void Elitism(vector<path> &nG, double eliteR) {
    for (int i = 0; i < eliteR; ++i) {
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

vector<path> crossover() {
    vector<path> newGen;
    path offSpring;
    int sbound, ebound;
    int pX, pY;
    while (newGen.size() <= populationSize - elitismRate) {
        set<int> ids;
        pX = chooseParent(ids);
        pY = chooseParent(ids);
        //Choose interval
        sbound = ran0to50(gen);
        do {
            ebound = ran0to50(gen);
        } while (sbound > ebound);
        offSpring = offspring(population[pX].route, population[pY].route, sbound, ebound);
        newGen.push_back(offSpring);
        offSpring = offspring(population[pY].route, population[pX].route, sbound, ebound);
        newGen.push_back(offSpring);
    }
    return newGen;
}

int mutated = 0;

void Mutation(vector<path> &pop, double mutationRate) {
    double r;
    int gene1, gene2;
    for (int i = 0; i < pop.size(); ++i) {
        r = ran0to1(gen);
        if (r <= mutationRate) {
            mutated++;
            gene1 = ran0to50(gen);
            do {
                gene2 = ran0to50(gen);
            } while (gene1 == gene2);
            int temp = pop[i].route[gene1];
            pop[i].route[gene1] = pop[i].route[gene2];
            pop[i].route[gene2] = temp;
            pop[i].fitness = fitnessCalculator(pop[i].route);
        }
    }
}


int main() {
    readInfo("..\\TSP51.txt");
    for (int i = 0; i < cityNum; ++i) {
        possibleNodes[i] = i + 1;
    }
    distanceCalculator();
    initPath(populationSize);
    int Step = 0;
    while (population[0].fitness > 400 && Step < 500000) {
        vector<path> newGEN = crossover();
        Mutation(newGEN, mutationRate);
        Elitism(newGEN, elitismRate);
        population.clear();
        population = newGEN;
        sort(population.begin(), population.end(), cmp);
        Step++;
        if (Step % 100 == 0) {
            cout << "mutate " << mutated << endl;
            cout << "Generation : " << Step << "\n\n";
            cout << "Population Fitness: " << endl;
            for (int i = 0; i < populationSize; ++i) {
                cout << population[i].fitness << " ";
            }
            cout << "\n\n" << "Fittest Path: " << "\n";
            for (int i = 0; i < cityNum; ++i) {
                cout << population[0].route[i] << ",";
            }
            cout << endl
                 << "-------------------------------------------------------------------------------------------------------------"
                 << endl;
        }
    }
    fstream file("..\\Results.txt", ::ios_base::app);
    string s;
    for (int i = 0; i < cityNum; ++i) {
        s += to_string(population[0].route[i]) + ",";
    }
    s += to_string(population[0].route[0]) + ",";
    s += to_string(population[0].fitness) + "\n";
    file << s;
    return 0;
}
