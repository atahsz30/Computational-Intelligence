#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int leftZero = 15, rightZero = 240, elitismRate = 5, populationSize = 25;
double mutationRate = 0.5;
random_device rd;
mt19937 gen(rd());
uniform_real_distribution<> ran0to1(0.0, 1.0);
uniform_real_distribution<> ran0to255(0, 255);
uniform_int_distribution<> ran0toPopSize(0, populationSize - 1);
vector<pair<int, int>> population(populationSize);

int chooseParent(set<int> &idxList) {
    int k = 5, idx;
    vector<pair<int, int>> candidates;
    for (int i = 0; i < k; ++i) {
        do {
            idx = ran0toPopSize(gen);
        } while (idxList.find(idx) != idxList.end());
        idxList.insert(idx);
        candidates.push_back(make_pair(population[idx].first, idx));
    }
    sort(candidates.begin(), candidates.end(), greater<>());
    return candidates[0].second;
}

pair<int, int> offspring(pair<int, int> parX, pair<int, int> parY) {
    int OS;
    int pX = parX.second, pY = parY.second;
    pX = pX & leftZero;
    pY = pY & rightZero;
    OS = pX + pY;
    return {pow(OS, 2), OS};
}

vector<pair<int, int>> crossover() {
    int x, y;
    pair<int, int> os1, os2;
    vector<pair<int, int>> newGen;
    while (newGen.size() < populationSize - elitismRate) {
        set<int> chosen;
        x = chooseParent(chosen);
        y = chooseParent(chosen);
        os1 = offspring(population[x], population[y]);
        newGen.push_back(os1);
        os2 = offspring(population[y], population[x]);
        newGen.push_back(os2);
    }
    return newGen;
}

void Elitism(vector<pair<int, int>> &nG, int eliteNUM) {
    for (int i = 0; i < eliteNUM; ++i) {
        nG.push_back(population[i]);
    }
}

bool stopEvolution() {
    bool stop = true;
    int instance = population[0].second;
    for (int i = 1; i < 5; ++i) {
        if (population[i].second != instance) {
            stop = false;
            break;
        }
    }
    return stop;
}

void mutation(vector<pair<int, int>> &newGen) {
    int gene;
    double r;
    for (int i = 0; i < newGen.size(); ++i) {
        r = ran0to1(gen);
        if (r <= mutationRate) {
            gene = rand() % 8;
            population[i].second ^= int(pow(2, gene));
            population[i].first = pow(population[i].second, 2);
        }
    }
}

void initializePeople() {
    for (int i = 0; i < population.size(); ++i) {
        int x = ran0to255(gen);
        population[i] = {int(pow(x, 2)), x};
    }
}


int main() {
    int gen = 0;
    initializePeople();
//    while (!stopEvolution()) {
    while (population[0].second < 255) {
        cout << "Generation: " << ++gen <<endl;
        vector<pair<int, int>> newGEN = crossover();
        mutation(newGEN);
        Elitism(newGEN, elitismRate);
        population.clear();
        population = newGEN;
        sort(population.begin(), population.end(), greater<>());
        cout << "Population Fitness: " <<endl;
        for (int i = 0; i < population.size(); ++i) {
            cout << population[i].second << " ";
        }
        cout << "\n\n";
    }
}
