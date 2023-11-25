package pointNsort;

public class pointNsort extends Element{
    public double[] points;
    public int dimension;

    @Override
    public double norm() {
        double result = 0;
        for (int i = 0; i < dimension; i++) {
            result += Math.pow(points[i], 2);
        }
        return result;
    }

    @Override
    public void print() {
        System.out.println("Dimension = " + dimension);
        System.out.println("Norm = " + norm());
    }

    public pointNsort(){        // Default Constructor
        dimension = 2;
        points = new double[2];
        points[0] = points[1] = 0;
    }

    public pointNsort(double[] __points){       // Parameterized Constructor
        dimension = __points.length;
        points = new double[dimension];
        System.arraycopy(__points, 0, points, 0, dimension);
    }


    public pointNsort(int dim){
        dimension = dim ;
        points = new double[dimension];
    }

    public void setRandomPoints(){
        for(int i=0;i< dimension;i++){
            points[i] = Math.round(Math.random() * 10);
        }
    }

    public void display(){
        for(int i=0;i<dimension;i++){
            System.out.println(points[i]);
        }
    }

    // Set points with specific values
    public void setPoints(double[] values) {
        if (values.length == dimension) {
            System.arraycopy(values, 0, points, 0, dimension);
        } else {
            System.out.println("Number of values provided doesn't match the dimension.");
        }
    }

    // Display points
    public void displayPoints() {
        System.out.println("Point coordinates: ");
        for (double coordinate : points) {
            System.out.println(coordinate);
        }
    }

    public double getX(){
        return points[0];
    }

    public double getY(){
        return points[1];
    }

    public double distFrom(pointNsort p){

        if(dimension != p.dimension){
            System.out.println("Cannot calculate distance: Dimensions do not match.");
            return -1;  // Or throw an exception
        }
        
        double sum = 0;
        
        for(int i=0;i<dimension;i++){
            double diff = points[i] - p.points[i];
            sum += Math.pow(diff, 2);
        }

        return Math.sqrt(sum);
    }

    public pointNsort midPoint(pointNsort p){
        if(dimension != p.dimension){
            System.out.println("Cannot calculate mid-point: Dimensions do not match.");
            return null;
        }

        pointNsort midPoints = new pointNsort();

        for(int i=0;i<dimension;i++){
            midPoints.points[i] = (points[i]-p.points[i])/2;
        }
        
        return midPoints;
    }

    // public static void main(String[] args) {
    //     pointNsort p1 = new pointNsort();
    //     pointNsort p2 = new pointNsort();
    //     p1.setRandomPoints();
    //     p2.setRandomPoints();

    //     pointNsort midPoint = p1.midPoint(p2);

    //     if (midPoint != null) {
    //         System.out.println("Mid-point coordinates:");
    //         midPoint.displayPoints();
    //     }

    //     // System.out.printf("Distance between the two points is: ",distance);

    // }
}