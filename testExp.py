

from expresiones import esExp


if __name__ == "__main__":

    test_true_exps = ["a",
                      "b",
                      "1",
                      "2",
                      "(b+(a+b))",
                      "(b+b)",
                      "(b+(a+(b==1)))",
                      "((a==((2==1)*b))*(a+(b==1)))",
                      "((a==((2==1)*b))*((a+a)+(b==1)))",
                      "((((a==(1*(b==a)))==a)==2)+(a+(b==1)))",
                      "(b+((2*2)+((b==1)==1)))"]

    test_false_exps = ["",
                      "$",
                      "b=b",
                      "(b==2",
                      "((((()))))",
                      "2*2)",
                      "(b+(ab))",
                      "(b+11)",
                      "(b+(a+(b=1)))",
                      "((a==((2==3)*b))*(a+(b==1)))",
                      "((a==((2==1)*b))*((a++a)+(b==1)))",
                      "((((a==(1*(b==a)))==a)k==2)+(a+(b==1)))",
                      "(a=b+c)"]

    # test esExp
    print("TRUE :")
    for exp in test_true_exps:
        print(exp, esExp(string=exp))

    print("\n")

    print("FALSE :")
    for exp in test_false_exps:
        print(exp, esExp(string=exp))
