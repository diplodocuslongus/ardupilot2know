import xmltodict
import pprint
import json

#with open('person.xml') as fd:
#    doc = xmltodict.parse(fd.read(), process_namespaces=True)

my_xml0 = """
    <audience>
      <id what="attribute">123</id>
      <name>Shubham</name>
    </audience>
    """

my_xml = """
    <enum name="MAV_TYPE">
      <entry value="0" name="MAV_TYPE_GENERIC">
        <description>Generic micro air vehicle.</description>
      </entry>
      <entry value="1" name="MAV_TYPE_FIXED_WING">
        <description>Fixed wing aircraft.</description>
      </entry>
      <entry value="2" name="MAV_TYPE_QUADROTOR">
        <description>Quadrotor</description>
      </entry>
      <entry value="3" name="MAV_TYPE_COAXIAL">
        <description>Coaxial helicopter</description>
      </entry>
      <entry value="4" name="MAV_TYPE_HELICOPTER">
        <description>Normal helicopter with tail rotor.</description>
      </entry>
      <entry value="5" name="MAV_TYPE_ANTENNA_TRACKER">
        <description>Ground installation</description>
      </entry>
      <entry value="6" name="MAV_TYPE_GCS">
        <description>Operator control unit / ground control station</description>
      </entry>
      <entry value="7" name="MAV_TYPE_AIRSHIP">
        <description>Airship, controlled</description>
      </entry>
      <entry value="8" name="MAV_TYPE_FREE_BALLOON">
        <description>Free balloon, uncontrolled</description>
      </entry>
      <entry value="9" name="MAV_TYPE_ROCKET">
        <description>Rocket</description>
      </entry>
      <entry value="10" name="MAV_TYPE_GROUND_ROVER">
        <description>Ground rover</description>
      </entry>
      <entry value="11" name="MAV_TYPE_SURFACE_BOAT">
        <description>Surface vessel, boat, ship</description>
      </entry>
      <entry value="12" name="MAV_TYPE_SUBMARINE">
        <description>Submarine</description>
      </entry>
      <entry value="13" name="MAV_TYPE_HEXAROTOR">
        <description>Hexarotor</description>
      </entry>
      <entry value="14" name="MAV_TYPE_OCTOROTOR">
        <description>Octorotor</description>
      </entry>
      <entry value="15" name="MAV_TYPE_TRICOPTER">
        <description>Tricopter</description>
      </entry>
      <entry value="16" name="MAV_TYPE_FLAPPING_WING">
        <description>Flapping wing</description>
      </entry>
      <entry value="17" name="MAV_TYPE_KITE">
        <description>Kite</description>
      </entry>
      <entry value="18" name="MAV_TYPE_ONBOARD_CONTROLLER">
        <description>Onboard companion controller</description>
      </entry>
      <entry value="19" name="MAV_TYPE_VTOL_DUOROTOR">
        <description>Two-rotor VTOL using control surfaces in vertical operation in addition. Tailsitter.</description>
      </entry>
      <entry value="20" name="MAV_TYPE_VTOL_QUADROTOR">
        <description>Quad-rotor VTOL using a V-shaped quad config in vertical operation. Tailsitter.</description>
      </entry>
      <entry value="21" name="MAV_TYPE_VTOL_TILTROTOR">
        <description>Tiltrotor VTOL</description>
      </entry>
      <!-- Entries up to 25 reserved for other VTOL airframes -->
      <entry value="22" name="MAV_TYPE_VTOL_RESERVED2">
        <description>VTOL reserved 2</description>
      </entry>
      <entry value="23" name="MAV_TYPE_VTOL_RESERVED3">
        <description>VTOL reserved 3</description>
      </entry>
      <entry value="24" name="MAV_TYPE_VTOL_RESERVED4">
        <description>VTOL reserved 4</description>
      </entry>
      <entry value="25" name="MAV_TYPE_VTOL_RESERVED5">
        <description>VTOL reserved 5</description>
      </entry>
      <entry value="26" name="MAV_TYPE_GIMBAL">
        <description>Onboard gimbal</description>
      </entry>
      <entry value="27" name="MAV_TYPE_ADSB">
        <description>Onboard ADSB peripheral</description>
      </entry>
    </enum>
"""
my_dict = xmltodict.parse(my_xml)
#print(my_dict)
print(my_dict['enum'])
print('\n\n')
print(my_dict['enum']['entry'])
print('\n\n')
print(my_dict['enum']['@name'])
print('\n\n')
for section in my_dict['enum']['entry']:
    tools_section = section.get('@name')
    print(tools_section)
#print(my_dict['enum']['entry']['name'])
#print(my_dict['enum']['id'])
#print(my_dict['audience']['id']['@what'])

