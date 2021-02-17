
#include <iostream>
#include <cmath>
using namespace std;
double no_coupon_price(double yield, int year) {
	return 100 / pow(1 + yield, year);
}

double first_deri_no(double yield, int year) {
	return (double(no_coupon_price(yield + double(0.000000001), year)) - no_coupon_price(yield, year)) / double(0.000000001);
}

float second_deri_no(float yield, int year) {
	//return (first_deri_no(yield+ 0.0000001,year)-first_deri_no(yield,year))/ 0.0000001;
	return (no_coupon_price(yield + 0.0000001, year) - 2 * no_coupon_price(yield, year) + no_coupon_price(yield - 0.0000001, year )) / (0.0000001 * 0.0000001);
}

double coupon_price(double yield, int year) {
	return 3 * ((1 - pow(1 + yield, -1 * year)) / yield) + 100 * pow(1 + yield, -1 * year);
}

double first_deri(double yield, int year) {
	return (double(coupon_price(yield + double(0.000000001), year)) - coupon_price(yield, year)) / double(0.000000001);
}

float second_deri(float yield, int year) {
	return (coupon_price(yield + 0.0000001, year) - 2 * coupon_price(yield, year) + coupon_price(yield - 0.0000001, year)) / (0.0000001 * 0.0000001);
}



void a() {
	cout << "(a):\n";
	float yield[6] = { 0.025, 0.026, 0.027, 0.03, 0.035, 0.04 };
	int year[6] = {1,2,3,5,10,30};
	for (int i = 0; i < 6; i++) {
		cout <<year[i]<<" " <<100/pow((1+yield[i]),year[i])<< "\n";
	}
	cout << "\n";
}

void b() {
	cout << "(b):\n";
	float yield[6] = { 0.025, 0.026, 0.027, 0.03, 0.035, 0.04 };
	int year[6] = { 1,2,3,5,10,30 };
	for (int i = 0; i < 6; i++) {
		cout << year[i] << " " << -1*first_deri_no(yield[i],year[i]) /no_coupon_price(yield[i],year[i]) << "\n";
	}
	

	
	cout << "\n";

}

void c() {
	cout << "(c):\n";
	float yield[6] = { 0.025, 0.026, 0.027, 0.03, 0.035, 0.04 };
	int year[6] = { 1,2,3,5,10,30 };
	for (int i = 0; i < 6; i++) {
		float price = 0;
		for (int j = 1; j <= year[i];j++) {
			price += 3 / pow((1 + yield[i]), j);
			//cout << i << " " << j <<" "<< price << "\n";
		}
		price += 100 / pow((1 + yield[i]), year[i]);
		//use formula
		float price_formula;
		price_formula = 3 * ((1 - pow(1 + yield[i], -1 * year[i])) / yield[i]) + 100 * pow(1 + yield[i], -1 * year[i]);
		
		cout << year[i] << " " << price<< "\n";
	}
	cout << "\n";

}

void d() {
	cout << "(d):\n";
	float yield[6] = { 0.025, 0.026, 0.027, 0.03, 0.035, 0.04 };
	int year[6] = { 1,2,3,5,10,30 };
	for (int i = 0; i < 6; i++) {
		
		cout << year[i] << " " << (-1)*first_deri(yield[i],year[i])/ coupon_price(yield[i], year[i]) <<"\n";
	}
	cout << "\n";

}

float* no_coupon_price_array(float * yield, int * year) {
	float r[6];
	for (int i = 0; i < 6; i++) {
		//cout << *(yield + i) << "\n";
		r[i] = 100 / pow(1 + *(yield+i), *(year+i));
	}
	return r;
}




void e() {
	cout << "(e):\n";
	float yield[6] = { 0.025, 0.026, 0.027, 0.03, 0.035, 0.04 };
	int year[6] = { 1,2,3,5,10,30 };
	for (int i = 0; i < 6; i++) {
		cout << second_deri_no(yield[i],year[i])/no_coupon_price(yield[i], year[i]) << endl;
	}
	cout << endl;
	for (int i = 0; i < 6; i++) {
		cout << second_deri(yield[i], year[i]) / coupon_price(yield[i], year[i]) << endl;
	}
	cout << "\n";
}

double  f(int year1, double yield1,int unit1, int year2, double yield2, int unit2,int year3, double yield3 , double unit3) {
	return unit1 * no_coupon_price(yield1, year1) + unit2 * no_coupon_price(yield2, year2) + unit3 * no_coupon_price(yield3, year3);
}
float deri(int year1, double yield1, double unit1, int year2, double yield2, int unit2, int year3, double yield3, double unit3) {
	return (double(f(year1, 0.0000001 +yield1, unit1,year2, 0.0000001 *yield2, unit2, year3, 0.0000001 +yield3,unit3)) - f(year1,  yield1,  unit1,  year2, yield2,unit2,year3, yield3,  unit3)) / 0.0000001;
}

float deri_2(int year1, double yield1, int unit1, int year2, double yield2, int unit2, int year3, double yield3, int unit3) {
	return (double(deri(year1, 0.0001 + yield1, unit1, year2, 0.0001 + yield2, unit2, year3, 0.0001 + yield3, unit3)) - 2 * double(deri(year1, yield1, unit1, year2, yield2, unit2, year3,  yield3, unit3)) + double(deri(year1, yield1- 0.0001, unit1, year2, yield2- 0.0001, unit2, year3, yield3- 0.0001, unit3))) / (0.0001 * 0.0001);
	//return (double(deri(year1, 0.001 + yield1, unit1, year2, 0.001 * yield2, unit2, year3, 0.001 + yield3, unit3)) - deri(year1, yield1, unit1, year2, yield2, unit2, year3, yield3, unit3)) / 0.001;
}



void g() {
	cout << "(g):\n" << double(-1)*deri(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -2)/f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -2) << " " << deri_2(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -2)/f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -2) <<endl;
}

double duration(int year1, double yield1, double unit1, int year2, double yield2, double unit2, int year3, double yield3, double unit3) {
	return double(-1) * deri(year1, yield1, unit1, year2, yield2, unit2, year3, yield3, unit3) / f(year1, yield1, unit1, year2, yield2, unit2, year3, yield3, unit3);
}

void h() {
	for (double i = -2; i <= -1.9987; i=i+0.000001) {
		cout <<i<<" "<< duration(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, i)<<" "<<f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, i) << endl;
	}
	
}

void i() {
	cout <<"(i): basis point change "<<(f(1, 0.025*1.01, 1, 3, 0.027*1.01, 1, 2, 0.026*1.01, -1.9982)- f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -1.9982))/ f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -1.9982) <<endl;
	//cout<< f(1, 0.025 * 1.01, 1, 3, 0.027 * 1.01, 1, 2, 0.026 * 1.01, -1.9982) <<endl;
	//cout<< f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -1.9982) <<endl;
}
void j() {
	cout << "(j): basis point change " <<" " <<(f(1, 0.025 * 0.99, 1, 3, 0.027 * 0.99, 1, 2, 0.026 * 0.99, -1.9982) - f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -1.9982)) / f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -1.9982) << endl;
	//cout<< f(1, 0.025 * 1.01, 1, 3, 0.027 * 1.01, 1, 2, 0.026 * 1.01, -1.9982) <<endl;
	//cout<< f(1, 0.025, 1, 3, 0.027, 1, 2, 0.026, -1.9982) <<endl;
}

double * k() {
	double cashflow[5];
	int principle = 100;
	for (int i = 0; i < 5; i++) {
		cashflow[i] = 20 + (100 - i * double(20)) * 0.03;
	}
	return cashflow;
}

double price_amortizing(double ytm) {
	double price = 0;
	for (int i = 0; i < 5; i++) {
		price += *(k() + i) / (1+ytm);
		//cout << price << endl;
	}
	return price;
}

double duration_amortizing(double ytm) {
	return (price_amortizing(ytm + 0.000000001) - price_amortizing(ytm)) / 0.000000001 / (-1) / price_amortizing(ytm);
}

void l() {
	cout <<"(l): Price: " <<price_amortizing(0.03) << endl;
	cout << "Duration: " << duration_amortizing(0.03) << endl;
}

int main(){
	a();
	b();
	c();
	b();
	d();
	e();
	cout<<"(f):\n"<<f(1,0.025,1,3,0.027,1,2,0.026,-2)<<endl<<endl;
	g();
	h();
	i();
	j();
	cout << "(k): Cashflows:";
	cout << *k()<<" "<< *(1+k()) << " "<< * (2+k()) << " "<< * (3+k()) << " "<< * (4+k()) << endl;
	l();
}

