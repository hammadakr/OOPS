package pointNsort;

import java.time.Duration;
import java.time.Instant;

public class SingleThreaded {

    public static final int[] SIZE = { 100, 1000, 10000, 100000, 1000000 };

    public static void single_threaded() {
        for (int k : SIZE) {
            pointNsort[] pointNsortArray = new pointNsort[k];
            for (int j = 0; j < k; j++) {
                int randomDimension = (int) (Math.floor(Math.random() * 10) + 2);
                pointNsortArray[j] = new pointNsort(randomDimension);
                pointNsortArray[j].setRandomPoints();
            }
            Instant start = Instant.now();
            merge_sort(pointNsortArray, 0, k - 1);
            Instant end = Instant.now();
            Duration timeElapsed = Duration.between(start, end);
            System.out.println("Time Elapsed for " + k + " = " + timeElapsed.toMillis());
        }
    }

    public static void merge_sort(pointNsort[] arr, int l, int r) {
        if (l < r) {
            int mid = l + (r - l) / 2;
            merge_sort(arr, l, mid);
            merge_sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
        }
    }

    public static void merge(pointNsort[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;
        pointNsort[] L = new pointNsort[n1];
        pointNsort[] R = new pointNsort[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i].norm() < R[j].norm()) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arr[k++] = L[i++];
        }
        while (j < n2) {
            arr[k++] = R[j++];
        }
    }

    public static void main(String[] args) {
        single_threaded();
        // test();
    }

    public static void test() {
        pointNsort[] pointNsortArray = new pointNsort[10];
        for (int i = 0; i < 10; i++) {
            int randomDimension = (int) (Math.floor(Math.random() * 10) + 2);
            pointNsortArray[i] = new pointNsort(randomDimension);
            pointNsortArray[i].setRandomPoints();
        }
        System.out.println("BEFORE SORTING");
        System.out.println("-----------------------------------------------------");
        for (pointNsort n : pointNsortArray) {
            n.print();
        }
        merge_sort(pointNsortArray, 0, 9);
        System.out.println("AFTER SORTING");
        System.out.println("-----------------------------------------------------");
        for (pointNsort n : pointNsortArray) {
            n.print();
        }
    }
}