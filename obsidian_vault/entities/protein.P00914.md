---
entity_id: "protein.P00914"
entity_type: "protein"
name: "phrB"
source_database: "UniProt"
source_id: "P00914"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phrB phr b0708 JW0698"
---

# phrB

`protein.P00914`

## Static

- Type: `protein`
- Source: `UniProt:P00914`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in repair of UV radiation-induced DNA damage. Catalyzes the light-dependent monomerization (300-600 nm) of cyclobutyl pyrimidine dimers (in cis-syn configuration), which are formed between adjacent bases on the same DNA strand upon exposure to ultraviolet radiation. phr encodes the DNA repair enzyme, deoxyribodipyrimidine photolyase (DNA photolyase; photoreactivating enzyme or PRE). DNA photolyase mediates blue-light dependent repair of cyclobutane pyrimidine dimers (CPDs; most commonly Thy<>Thy) which are produced by exposure of cells to UV radiation at 200-300nm. Early studies on photoreactivation (PR) were conducted using E. coli B strains (see for example ). phr has been cloned and its protein product purified. The active, purified enzyme is a monomer and repairs UV-irradiated DNA (UV-pBR322) in a light dependent reaction; the enzyme contains two prosthetic groups - a light harvesting cofactor or antenna pigment, 5,10-methenyltetrahydrofolate polyglutamate (see 5-10-METHENYL-THF-GLU-N), and a catalytic flavin adenine dinucleotide (FAD) cofactor (active in the FADH- form in vivo)...

## Biological Role

Catalyzes cyclobutadipyrimidine (in DNA) pyrimidine-lyase (reaction.R00034), RXN-19242 (reaction.ecocyc.RXN-19242), RXN-19245 (reaction.ecocyc.RXN-19245), RXN-20897 (reaction.ecocyc.RXN-20897). Bound by a 5,10-methenyltetrahydrofolate (molecule.ecocyc.5-10-METHENYL-THF-GLU-N), FADH (molecule.ecocyc.FADH).

## Annotation

FUNCTION: Involved in repair of UV radiation-induced DNA damage. Catalyzes the light-dependent monomerization (300-600 nm) of cyclobutyl pyrimidine dimers (in cis-syn configuration), which are formed between adjacent bases on the same DNA strand upon exposure to ultraviolet radiation.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00034|reaction.R00034]] `KEGG` `database` - via EC:4.1.99.3
- `catalyzes` --> [[reaction.ecocyc.RXN-19242|reaction.ecocyc.RXN-19242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19245|reaction.ecocyc.RXN-19245]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20897|reaction.ecocyc.RXN-20897]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.5-10-METHENYL-THF-GLU-N|molecule.ecocyc.5-10-METHENYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.FADH|molecule.ecocyc.FADH]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0708|gene.b0708]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00914`
- `KEGG:ecj:JW0698;eco:b0708;ecoc:C3026_03540;`
- `GeneID:947005;`
- `GO:GO:0000719; GO:0003677; GO:0003684; GO:0003904; GO:0007603; GO:0009416; GO:0071949`
- `EC:4.1.99.3`

## Notes

Deoxyribodipyrimidine photo-lyase (EC 4.1.99.3) (DNA photolyase) (Photoreactivating enzyme)
