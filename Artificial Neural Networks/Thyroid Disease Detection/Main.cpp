#include <bits/stdc++.h>

using namespace std;

vector<vector<double>> readData(string address) {
    ifstream file(address);
    string line;
    vector<vector<double>> data;
    if (!file.is_open()) {
        cerr << "Error opening file." << endl;
    }
    while (getline(file, line)) {
        stringstream ss(line);
        string value;
        vector<double> row;
        while (getline(ss, value, ',')) {
            row.push_back(stod(value));
        }
        data.push_back(row);
    }
    file.close();
    return data;
}


const int epoch = 100, h_neu_size = 10, out_size = 3;
const double alpha = 0.003;

vector<double> y(out_size), z(h_neu_size);
vector<double> w_bias(out_size), v_bias(h_neu_size);
vector<double> w_delta(out_size), v_delta(h_neu_size);
vector<vector<double>> x, target, v(h_neu_size), w(out_size);


void initialize(vector<vector<double>> &vec) {
    for (int i = 0; i < vec.size(); ++i) {
        for (int j = 0; j < vec[0].size(); ++j) {
            vec[i][j] = (rand() / double(RAND_MAX)) + 0.5;
        }
    }

}

void normalize(vector<vector<double>> &ini) {
    double mini, maxi;
    for (int i = 0; i < ini.size(); ++i) {
        mini = *min_element(ini[i].begin(), ini[i].end());
        maxi = *max_element(ini[i].begin(), ini[i].end());
        for (int j = 0; j < ini[0].size(); ++j) {
            ini[i][j] = (ini[i][j] - mini) / (maxi - mini);
        }
    }
}

double sigmoid(double in) {
    return 1 / (1 + pow(M_E, -in));
}

double derived(double in) {
    return sigmoid(in) * (1 - sigmoid(in));
}

void forwardPass(vector<double> xx, vector<vector<double>> weights, vector<double> bias, vector<double> &yy) {
    for (int i = 0; i < yy.size(); ++i) {
        double sum = 0;
        for (int j = 0; j < xx.size(); ++j) {
            sum += xx[j] * weights[i][j];
        }
        yy[i] = sum + bias[i];
    }
}

void backPropagate(vector<double> xx, vector<vector<double>> &weights, vector<double> &bias, vector<double> delta) {
    for (int i = 0; i < delta.size(); ++i) {
        for (int j = 0; j < xx.size(); ++j) {
            weights[i][j] += alpha * delta[i] * xx[j];
        }
    }
    for (int i = 0; i < bias.size(); ++i) {
        bias[i] += alpha * delta[i];
    }

}

void Train() {
    x = readData("..\\InData.txt");
    target = readData("..\\OutData.txt");
    fill(v.begin(), v.end(), vector<double>(x[0].size()));
    initialize(v);
    fill(w.begin(), w.end(), vector<double>(z.size()));
    fill(v_bias.begin(), v_bias.end(), 0.2);
    fill(w_bias.begin(), w_bias.end(), 0.2);
    for (int e = 0; e < epoch; e++) {
        int c3 = 0, c2 = 0, c1 = 0, h = 0;
        for (int data = 0; data < x.size(); ++data) {
            if (target[data][2] == 1 && c3 > 1500) continue;
            if (target[data][2] == 1) c3++;
            if (target[data][1] == 1 && c2 > 501) continue;
            if (target[data][1] == 1) c2++;
            if (target[data][0] == 1 && c1 > 501) continue;
            if (target[data][0] == 1) c1++;
//            if (target[data][0] == 1) cout <<"d:  "<< data<<endl;

            h++;
            // Forward
            forwardPass(x[data], v, v_bias, z);
            forwardPass(z, w, w_bias, y);
            // Loss and Back Propagate
            for (int i = 0; i < w_delta.size(); ++i) {
                w_delta[i] = (target[data][i] - sigmoid(y[i])) * derived(y[i]);
            }
            backPropagate(z, w, w_bias, w_delta);
            for (int i = 0; i < v_delta.size(); ++i) {
                double D = 0;
                for (int j = 0; j < w_delta.size(); ++j) {
                    D += w_delta[j] * w[j][i];
                }
                v_delta[i] = D * derived(z[i]);
            }
            backPropagate(x[data], v, v_bias, v_delta);
        }
    }
}

void Test_valid(string input, string output) {
    vector<int> eachClassNum(out_size, 0);
    vector<int> all(out_size), True(out_size);
    x = readData(input);
    target = readData(output);
    for (int data = 0; data < x.size(); data++) {
        double pos[out_size];
        double sum = 0, maxP = 0, maxTg = 0;
        int idP, idTg;
        forwardPass(x[data], v, v_bias, z);
        forwardPass(z, w, w_bias, y);
        for (int i = 0; i < out_size; ++i) {
            pos[i] = pow(M_E, y[i]);
            sum += pos[i];
        }
        for (int i = 0; i < out_size; ++i) {
            pos[i] = (pos[i] / sum) * 100;
//            cout << pos[i] << ",  ";
        }
        for (int i = 0; i < out_size; ++i) {
            if (pos[i] > maxP) {
                maxP = pos[i];
                idP = i + 1;
            }
            if (target[data][i] > maxTg) {
                maxTg = target[data][i];
                idTg = i + 1;
                eachClassNum[idTg - 1]++;
            }
        }
//        cout << "Pred: " << idP << ",  " << "Target: " << idTg << endl;
        all[idTg - 1]++;
        if (idP == idTg) True[idTg - 1]++;
    }
    for (int i = 0; i < out_size; ++i) {
        cout << "Class " << i + 1 << endl;
        cout << "accuracy: " << (True[i] / double(all[i])) << ", True Prediction: " << True[i] << ", class size: "
             << eachClassNum[i] << endl;
    }

}

int main() {
    Train();
    Test_valid("..\\TestIN.txt", "..\\TestOut.txt");
    return 0;
}
