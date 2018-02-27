public class Algorithms_Main {

    public static void main(String[] args) {
        // Big O notation - Gives us a way of comparing the time complexity (number of steps taken to complete the algorithm)
        // of different algorithms independent of hardware.
        // Order of increasing Time Complexity (Top to Bottom) (We take the worst case scenario for Time Complexity.

        // O(1) Constant Time Complexity.
        O_of_1();

        // O(log(n)) Logarithmic Time Complexity.
        // Binary Search

        // O(n) Linear Time Complexity.
        // Linear Search

        // O(n^2) Quadratic Time Complexity.
        // Nested for loops
        O_of_n2();
    }


    // O(1) [ Constant ] Algorithm
    private static void O_of_1() {
        // O(1) has constant number of steps regardless of the input size.
        // some examples of O(1) is accessing a specific index of an array
        // The time to retrieve an element will be the same no matter where the element is in the array.
        // Any expression is considered O(1) and takes "1 step"

        // Create an array of size 10, and populate it with numbers 1 - 10.
        int[] intArray = new int[10];

        for (int i=0; i<intArray.length; i++) {
            intArray[i] = i + 1;
        }

        // we can now access any location of the array and the Time Complexity will be the same.
        System.out.println(intArray[5]);

        // O(1) are the fastest in terms of time complexity since it will always take the same number of steps regardless of the input size.
    }


    // O(n^2) [ Quadratic ] Algorithm
    private static void O_of_n2() {
        // Nested For loops
        // Our movie theater app is an example of O(n^2) since we need to check each element in each row and column to see if the seat is taken

        int[] matrix1 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int[] matrix2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        // Each array contains 10 elements find the sum of each multiple for each element in both of the arrays.
        // Our Time Complexity increases by n^2 as our arrays increase in size.

        int total = 0;
        for (int x : matrix1) {
            for (int y: matrix2) {
                total += x * y;
                // System.out.println("Total in this iteration is: " + total);
            }
            // System.out.println("X is now: " + x);
        }
        System.out.println("Our total is: " + total);
    }
}
