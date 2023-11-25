package pointN;

public class pointN extends Element{
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

    public pointN(){        // Default Constructor
        dimension = 2;
        points = new double[2];
        points[0] = points[1] = 0;
    }

    public pointN(double[] __points){       // Parameterized Constructor
        dimension = __points.length;
        points = new double[dimension];
        System.arraycopy(__points, 0, points, 0, dimension);
    }


    public pointN(int dim){
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

    public double distFrom(pointN p){

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

    public pointN midPoint(pointN p){
        if(dimension != p.dimension){
            System.out.println("Cannot calculate mid-point: Dimensions do not match.");
            return null;
        }

        pointN midPoints = new pointN();

        for(int i=0;i<dimension;i++){
            midPoints.points[i] = (points[i]-p.points[i])/2;
        }
        
        return midPoints;
    }

    public static void main(String[] args) {
        pointN p1 = new pointN();
        pointN p2 = new pointN();
        p1.setRandomPoints();
        p2.setRandomPoints();

        pointN midPoint = p1.midPoint(p2);

        if (midPoint != null) {
            System.out.println("Mid-point coordinates:");
            midPoint.displayPoints();
        }

        // System.out.printf("Distance between the two points is: ",distance);

    }
}