import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public static int getDayNumberOld(Date date, Calendar cal) {
	cal.setTime(date);
	return cal.get(Calendar.DAY_OF_WEEK); // 1 = Sunday, 7 = Saturday
}

public static int findFirstWednesday(Calendar cal) {
	int date = cal.get(Calendar.DATE)
	int dayofweek = cal.get(Calendar.DAY_OF_WEEK)
	int daystil = 0
	if(dayofweek != 4) {
		if(dayofweek < 4)
		{
			daystil = 4-dayofweek;
		}
		else if(dayofweek > 4)
		{
			daystil = dayofweek-4
		}
	int wed1 = date + daystil;
	return wed1;
}
public static int[] generateWednesdays(int wed1) {
	int[] weds = new int[2]

	wed2 = wed1+7;
	wed4 = wed2+14;

	weds[0] = wed2
	weds[1] = wed4
	return weds;
}

public static void main(String[] args)
{
	String reply = "y";
	while(reply.equals("y"))
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Gathering date data...")
		Calendar cal = Calendar.getInstance();

		int[] weds = generateWednesdays(findFirstWednesday(cal));

		System.out.println("The second Wednesday of the month's date will be: ", weds[0]);
		print("\nThe fourth Wednesday of this month's date will be: ", weds[1]);
		System.out.println("Replay? [y/n]");
		reply = s.nextLine();
	}

}

/*
if day != Wednesday
	days til wednesday = 0
	while (otherday != Wednesday)
		daystil += 1
		otherday = getday(day+daystil)
	secondwed = currentdate + daystil
	fourthwed = secondwed + 14
*/



/*dishes = mon, wed, fri
floors, bathrooms, surfaces = 2nd/4th wed
trash, recycling = wed, sun
refrigerator = 3rd fri*/