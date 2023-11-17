public class Point2D extends Element2D{
    public double x;
    public double y;

    @Override
    public double norm() {
        return Math.sqrt(x * x + y * y);
    }

    @Override
    public void print(){
        System.out.println("X = " + x);
        System.out.println("Y = " + y);
        System.out.println("Norm = " + norm());
    }

    public Point2D() {        // Default Constructor
        x = y = 0;
    }

    public Point2D(double x, double y) {  // Parameterized Constructor
        this.x = x;
        this.y = y;
    }

    public void setRandomPoints() {
        x = Math.round(Math.random() * 10);
        y = Math.round(Math.random() * 10);
    }

    public void display() {
        System.out.println("X = " + x);
        System.out.println("Y = " + y);
    }

    // Set points with specific values
    public void setPoints(double newX, double newY) {
        x = newX;
        y = newY;
    }

    // Display points
    public void displayPoints() {
        System.out.println("Point coordinates: ");
        System.out.println("X = " + x);
        System.out.println("Y = " + y);
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double distFrom(Point2D p) {
        double diffX = x - p.x;
        double diffY = y - p.y;
        return Math.sqrt(diffX * diffX + diffY * diffY);
    }

    public Point2D midPoint(Point2D p) {
        Point2D midPoint = new Point2D();
        midPoint.x = (x + p.x) / 2;
        midPoint.y = (y + p.y) / 2;
        return midPoint;
    }

    public static void main(String[] args) {
        Point2D p1 = new Point2D();
        Point2D p2 = new Point2D();
        p1.setRandomPoints();
        p2.setRandomPoints();

        Point2D midPoint = p1.midPoint(p2);

        if (midPoint != null) {
            System.out.println("Mid-point coordinates:");
            midPoint.displayPoints();
        }
    }
}
