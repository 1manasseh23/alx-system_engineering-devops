#!/usr/bin/env bash
#This is to install flask from pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
