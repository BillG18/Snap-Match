"""Prototype for color matching functions."""
import colorsys


def RGB255(RGB):
    """Help function to convert RGB to 255 scale."""
    return [round((RGB[0]*255), 2),
            round((RGB[1]*255), 2),
            round((RGB[2]*255), 2)]


def complementary(R, G, B):
    """Calculate complementery color from RGB values (0-255)."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS = [((HLS[0] + 0.5) % 1), HLS[1], HLS[2]]
    RGB = colorsys.hls_to_rgb(HLS[0], HLS[1], HLS[2])
    return RGB255(RGB)


def analagous(R, G, B):
    """Calculate analagous colors, returns 2 colors."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS_1 = [((((HLS[0]*360) + 30) % 360)/360), HLS[1], HLS[2]]
    HLS_2 = [((((HLS[0]*360) - 30) % 360)/360), HLS[1], HLS[2]]
    RGB_1 = colorsys.hls_to_rgb(HLS_1[0], HLS_1[1], HLS_1[2])
    RGB_2 = colorsys.hls_to_rgb(HLS_2[0], HLS_2[1], HLS_2[2])
    return [RGB255(RGB_1), RGB255(RGB_2)]


def triadic(R, G, B):
    """Calculate triadic colors, returns 2 colors."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS_1 = [((((HLS[0]*360) + 120) % 360)/360), HLS[1], HLS[2]]
    HLS_2 = [((((HLS[0]*360) - 120) % 360)/360), HLS[1], HLS[2]]
    RGB_1 = colorsys.hls_to_rgb(HLS_1[0], HLS_1[1], HLS_1[2])
    RGB_2 = colorsys.hls_to_rgb(HLS_2[0], HLS_2[1], HLS_2[2])
    return [RGB255(RGB_1), RGB255(RGB_2)]


def split_complementary(R, G, B):
    """Calculate split-complementary colors, returns 2 colors."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS = [((HLS[0] + 0.5) % 1), HLS[1], HLS[2]]
    RGB = colorsys.hls_to_rgb(HLS[0], HLS[1], HLS[2])
    HLS_1 = [((((HLS[0]*360) + 30) % 360)/360), HLS[1], HLS[2]]
    HLS_2 = [((((HLS[0]*360) - 30) % 360)/360), HLS[1], HLS[2]]
    RGB_1 = colorsys.hls_to_rgb(HLS_1[0], HLS_1[1], HLS_1[2])
    RGB_2 = colorsys.hls_to_rgb(HLS_2[0], HLS_2[1], HLS_2[2])
    return [RGB255(RGB_1), RGB255(RGB_2)]


if __name__ == '__main__':
    print complementary(255, 0, 255)
    print analagous(255, 0, 255)
    print triadic(255, 0, 255)
    print split_complementary(255, 0, 255)


"""
Generic RGB to HLS converter

var_R = ( R / 255 )                     //RGB from 0 to 255
var_G = ( G / 255 )
var_B = ( B / 255 )

var_Min = min( var_R, var_G, var_B )    //Min. value of RGB
var_Max = max( var_R, var_G, var_B )    //Max. value of RGB
del_Max = var_Max - var_Min             //Delta RGB value

V = var_Max

if ( del_Max == 0 )                     //This is a gray, no chroma...
{
   H = 0                                //HSV results from 0 to 1
   S = 0
}
else                                    //Chromatic data...
{
   S = del_Max / var_Max

   del_R = ( ( ( var_Max - var_R ) / 6 ) + ( del_Max / 2 ) ) / del_Max
   del_G = ( ( ( var_Max - var_G ) / 6 ) + ( del_Max / 2 ) ) / del_Max
   del_B = ( ( ( var_Max - var_B ) / 6 ) + ( del_Max / 2 ) ) / del_Max

   if      ( var_R == var_Max ) H = del_B - del_G
   else if ( var_G == var_Max ) H = ( 1 / 3 ) + del_R - del_B
   else if ( var_B == var_Max ) H = ( 2 / 3 ) + del_G - del_R

   if ( H < 0 ) H += 1
   if ( H > 1 ) H -= 1
}
"""
