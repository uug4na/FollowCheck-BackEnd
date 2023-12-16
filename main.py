import requests
import json
import re

class InstagramProfile:
    def __init__(self, username):
        self.username = username
        self.profile_id = None

    def get_id(self):
        url = f"https://www.instagram.com/{self.username}/"
        resp = requests.get(url)
        resp.raise_for_status()
        pattern = r'"profilePage_([\d]+)"'
        match = re.search(pattern, resp.text)
        if match:
            self.profile_id = match.group(1)
            print(f"Profile ID for {self.username}: {self.profile_id}")
            self.follow_count(self.profile_id)
        else:
            print(f"Profile ID not found on {self.username}'s profile page.")

    def follow_count(self, profile_id):
        url = "https://www.instagram.com:443/api/graphql"
        headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Brave\";v=\"120\"", "X-Ig-App-Id": "936619743392459", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "X-Fb-Friendly-Name": "PolarisUserHoverCardStatisticsSectionQuery", "X-Fb-Lsd": "1wKcSJjTsiu5NkjTn__1GI", "Sec-Ch-Ua-Platform-Version": "\"14.0.0\"", "Content-Type": "application/x-www-form-urlencoded", "X-Asbd-Id": "129477", "X-Csrftoken": "ZOdUB17e2eZtpEEt801op3gegxejMWZz", "Sec-Ch-Ua-Model": "\"\"", "Sec-Ch-Ua-Platform": "\"macOS\"", "Accept": "*/*", "Sec-Gpc": "1", "Accept-Language": "en-US,en;q=0.6", "Origin": "https://www.instagram.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate, br"}
        data = {"av": "17841429964935478", "__d": "www", "__user": "0", "__a": "1", "__req": "1i", "__hs": "19707.HYP:instagram_web_pkg.2.1..0.1", "dpr": "2", "__ccg": "UNKNOWN", "__rev": "1010466952", "__s": "flphox:mrmb21:00ctp0", "__hsi": "7313282678413537522", "__dyn": "7xeUjG1mxu1syUbFp60DU98nwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO2O1Vw8G1nzUO0n24oaEd86a3a1YwBgao6C0Mo2iyovw8OfK0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azqwt8dUaob82cwMwrUdUbGwmk1xwmo6O1FwlE6OFA6fxy4Ujw", "__csr": "gbYj24cjiW8BOhIIzhyOSB8IK_LV4y8FvJamhkK_UC_rQCuENWJ4rBAhpp8K_zdmujG-ppqBzmmXFdkmFamigHDGdVSqcoyV6iHBDV8N38OEjx29Jyqx13onxGGFaE01cu941UJw1mOhU0nNw1SIOj9hk4Bp83Vxqq6E6-0OE5S9wKg2pw9C0ke0Fo3GIBwrUy79QaBg3NwLCwjU0NeEgx22K6u2kU5K00GfE", "__comet_req": "7", "fb_dtsg": "NAcNDLRN2-R0PswTMPqbu2btBK2D2iRusCv9j8dRse-nmAneW9DLtpA:17843729647189359:1699628657", "jazoest": "26211", "lsd": "1wKcSJjTsiu5NkjTn__1GI", "__spin_r": "1010466952", "__spin_b": "trunk", "__spin_t": "1702756313", "fb_api_caller_class": "RelayModern", "fb_api_req_friendly_name": "PolarisUserHoverCardStatisticsSectionQuery", "variables": f"{{\"userID\":\"{profile_id}\"}}", "server_timestamps": "true", "doc_id": "6697821680334660"}
        resp = requests.post(url, headers=headers, data=data).text
        resp = json.loads(resp)
        follower_count = resp['data']['fetch__XDTUserDict']['follower_count']
        following_count = resp['data']['fetch__XDTUserDict']['following_count']
        print(f"Follower Count: {follower_count}")
        print(f"Following Count: {following_count}")

class getNames:
    def __init__(self, follower_count, following_count):
        self.werCount = follower_count
        self.ingCount = following_count
    
    def followingNames(self):
        tmp = self.ingCount // 200
        print(tmp)
        

if __name__ == "__main__":
    instagram_profile = InstagramProfile("osiris.leet")
    instagram_profile.get_id()
    print("ANOTHER PART:")
    # names = getNames(follower_count, following_count)
