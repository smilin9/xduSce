# created by: smilin9
# time: 2022-12-13 18:38:59


import libnum
from Crypto.Util.number import long_to_bytes
from gmpy2 import invert

n0 = 0x8496396a0973fea57cda4bbe85f9d134244a21e7132735908ba604ae75227f613
p0 = 275127860351348928173285174381581152299
q0 = 3487583947589437589237958723892346254777
c0 = 0x28a34a6a3695d6aff1524aed642f5e60c103952ad23c6746c36e19a4606a9cac7
e0 = 65537

n = 0x00b0bee5e3e9e5a7e8d00b493355c618fc8c7d7d03b82e409951c182f398dee3104580e7ba70d383ae5311475656e8a964d380cb157f48c951adfa65db0b122ca40e42fa709189b719a4f0d746e2f6069baf11cebd650f14b93c977352fd13b1eea6d6e1da775502abff89d3a8b3615fd0db49b88a976bc20568489284e181f6f11e270891c8ef80017bad238e363039a458470f1749101bc29949d3a4f4038d463938851579c7525a69984f15b5667f34209b70eb261136947fa123e549dfff00601883afd936fe411e006e4e93d1a00b0fea541bbfc8c5186cb6220503a94b2413110d640c77ea54ba3220fc8f4cc6ce77151e29b3e06578c478bd1bebe04589ef9a197f6f806db8b3ecd826cad24f5324ccdec6e8fead2c2150068602c8dcdc59402ccac9424b790048ccdd9327068095efa010b7f196c74ba8c37b128f9e1411751633f78b7b9e56f71f77a1b4daad3fc54b5e7ef935d9a72fb176759765522b4bbc02e314d5c06b64d5054b7b096c601236e6ccf45b5e611c805d335dbab0c35d226cc208d8ce4736ba39a0354426fae006c7fe52d5267dcfb9c3884f51fddfdf4a9794bcfe0e1557113749e6c8ef421dba263aff68739ce00ed80fd0022ef92d3488f76deb62bdef7bea6026f22a1d25aa2a92d124414a8021fe0c174b9803e6bb5fad75e186a946a17280770f1243f4387446ccceb2222a965cc30b3929
c1 = 0xe2656d98064060e2d223768e65ddaf83b031c12b1764c02a200ea358d621a1df50dce5aa4058aaffc9471bb8cafd609f4093adc71167775ecaf53e77b08fee395855e833f6da9060d10dd7534937e7136323588bc76905a284f1bbef30fc8723ef804eeafaf40d42227b0aaf213dcdb1a84aafb8aa0f96a132c648cb2eace527c2510e3c17e071543229f69ede7ec97e511d15b90b6e908440b07c19bd5f8db4fa225cc1e790331
c2 = 0xafd609e652925da44893025767bb57f11fd49ee7f1d6b63d21a9aab22e70ea91e404386cf57fc79f00629512592cf827c21147297f773f0c12912274d747ed81b4e8dfef01f6f71259dd5c9c2b9ffbfe7450fa2eaf9a3e932c0c877f374471d8651d75f5bb5769fcbfbb837636385dadd70db774fafecb6f2812c1fc2e06cd73404ae9859e5d30fe2dcf906067325ef6407b01de7093c3d11685b31b8b924cac7ee5e0444deeff2190875edcc4e4f9d4e991a083dd946b5ad53ecc53f963b5211c57e9a78aa717763c45a4ba1c1bfac7687bc0e6e5c1b452faf9232f30356214746fbb625d20a693d32bf665232daeb82f8460d5b38355ca2a0226e89f12f0d12bf09bd581274c5ed47ab1d1caf1e25a37f974c1f0808ae0984108ff69047abbca7f45430b260036d93a318625dfab0e8c3172db0a58496c0f47ac8af3cc425686f4233d085e88f81680a78a9213405be118f83017ad6c8a5908d1cb584ec8334c125305d32e17fd2cdf07cb0f06c8b16940b6e171ddfdffd55cee5d72002b66d4102243dab3dcfa21b5d12b384820ac1a1ba4f83ce8b6c8f3e8cedd8af42ed085bac111763d416a61b22eed6c5aa52af01851607de198ea1297e4aa9343afefa475f63b5d8502b9952d8008227f24fa2331254851dd5e9415ca7ad5a255fc5d74ead231f9e360040ff5ee5968d696a264bf6fdf09e7ad28584690f5cc311494
e1 = 17
e2 = 65537


def dem1(n0, p0, q0, c0, e0):
    d0 = libnum.invmod(e0, (p0 - 1) * (q0 - 1))
    m1 = pow(c0, d0, n0)  # m1 的十进制形式
    m1 = long_to_bytes(m1)  # m1明文
    print("m1=%s" % m1)  # 结果为 b‘ m1 ’ 的形式


def dem2(n, c1, c2, e1, e2):

    def egcd(a, b):
        if b == 0:
            return a, 0
        else:
            x, y = egcd(b, a % b)
            return y, x - (a // b) * y

    s = egcd(e1, e2)
    s1 = s[0]
    s2 = s[1]
    # 求模反元素
    if s1 < 0:
        s1 = -s1
        c1 = invert(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = invert(c2, n)
    m2 = pow(c1, s1, n) * pow(c2, s2, n) % n
    m2 = long_to_bytes(m2)  # m2明文
    print("m2=%s" % m2)  # 结果为 b‘ m2 ’ 的形式


dem1(n0, p0, q0, c0, e0)
dem2(n, c1, c2, e1, e2)
