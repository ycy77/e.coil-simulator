---
entity_id: "protein.P0A776"
entity_type: "protein"
name: "rppH"
source_database: "UniProt"
source_id: "P0A776"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rppH nudH ygdP b2830 JW2798"
---

# rppH

`protein.P0A776`

## Static

- Type: `protein`
- Source: `UniProt:P0A776`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Master regulator of 5'-end-dependent mRNA decay (PubMed:18202662). Accelerates the degradation of transcripts by removing pyrophosphate from the 5'-end of triphosphorylated RNA, leading to a more labile monophosphorylated state that can stimulate subsequent ribonuclease cleavage (PubMed:18202662). Preferentially hydrolyzes diadenosine penta-phosphate with ATP as one of the reaction products (PubMed:11479323). Also able to hydrolyze diadenosine hexa- and tetra-phosphate (PubMed:11479323). Has no activity on diadenosine tri-phosphate, ADP-ribose, NADH and UDP-glucose (PubMed:11479323). In an RNase PH (rph) wild-type strain background, RppH is not required for maturation of tRNAs; however, strains with the truncated rph allele (for example K12 W1485 and its derivatives MG1655 and W3110) require RppH for maturation of certain monocistronic tRNAs with short (<5 nucleotides) leader sequences (PubMed:28808133). In the meningitis causing strain E.coli K1, has been shown to play a role in HBMEC (human brain microvascular endothelial cells) invasion in vitro (PubMed:10760174). {ECO:0000269|PubMed:10760174, ECO:0000269|PubMed:11479323, ECO:0000269|PubMed:18202662, ECO:0000269|PubMed:28808133}. RppH is an RNA pyrophosphohydrolase that initiates mRNA degradation by hydrolysis of the 5'-triphosphate end, preparing mRNAs for further degradation by CPLX0-3461 and the CPLX0-2381...

## Biological Role

Catalyzes RXN0-5510 (reaction.ecocyc.RXN0-5510), RXN0-7283 (reaction.ecocyc.RXN0-7283). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Master regulator of 5'-end-dependent mRNA decay (PubMed:18202662). Accelerates the degradation of transcripts by removing pyrophosphate from the 5'-end of triphosphorylated RNA, leading to a more labile monophosphorylated state that can stimulate subsequent ribonuclease cleavage (PubMed:18202662). Preferentially hydrolyzes diadenosine penta-phosphate with ATP as one of the reaction products (PubMed:11479323). Also able to hydrolyze diadenosine hexa- and tetra-phosphate (PubMed:11479323). Has no activity on diadenosine tri-phosphate, ADP-ribose, NADH and UDP-glucose (PubMed:11479323). In an RNase PH (rph) wild-type strain background, RppH is not required for maturation of tRNAs; however, strains with the truncated rph allele (for example K12 W1485 and its derivatives MG1655 and W3110) require RppH for maturation of certain monocistronic tRNAs with short (<5 nucleotides) leader sequences (PubMed:28808133). In the meningitis causing strain E.coli K1, has been shown to play a role in HBMEC (human brain microvascular endothelial cells) invasion in vitro (PubMed:10760174). {ECO:0000269|PubMed:10760174, ECO:0000269|PubMed:11479323, ECO:0000269|PubMed:18202662, ECO:0000269|PubMed:28808133}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5510|reaction.ecocyc.RXN0-5510]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7283|reaction.ecocyc.RXN0-7283]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2830|gene.b2830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A776`
- `KEGG:ecj:JW2798;eco:b2830;ecoc:C3026_15535;`
- `GeneID:75172914;75203778;947300;`
- `GO:GO:0000287; GO:0005737; GO:0006402; GO:0008033; GO:0016818; GO:0034353; GO:0050779; GO:0110153; GO:0110154; GO:0110155`
- `EC:3.6.1.-`

## Notes

RNA pyrophosphohydrolase (EC 3.6.1.-) ((Di)nucleoside polyphosphate hydrolase) (Ap5A pyrophosphatase)
