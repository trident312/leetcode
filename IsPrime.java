
import java.util.Scanner;

public class IsPrime {


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a test integer: ");
        int value = scan.nextInt();

        double prime;
        boolean test = false;

        for (int i = 2; i <= Math.sqrt(value); i++){
            prime = value % i;
            if (prime == 0){
                test = false;
                break;
            }
            else {
                test = true;
            }


        }

        if (!test){
            System.out.println(value + " is not a prime number");
        }

        if (test){
            System.out.println(value + " is a prime number");
        }



    }


}
