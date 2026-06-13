---
entity_id: "protein.P0CG19"
entity_type: "protein"
name: "rph"
source_database: "UniProt"
source_id: "P0CG19"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rph orfE b3643 JW3618"
---

# rph

`protein.P0CG19`

## Static

- Type: `protein`
- Source: `UniProt:P0CG19`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This an expressed but non-active exoribonuclease allele (PubMed:8501045). The catalytically inactive protein translated in strain K12 MG1655 inhibits the 5'-processing of primary pre-tRNAs with short (<5 nucleotide) leaders in a dominant-negative effect when RNA pyrophosphohydrolase (rppH) is also inactive; perhaps inactive Rph inhibits interaction with RNase P which is exacerbated when RppH cannot cleave the triphosphate of the primary transcript (PubMed:28808133). {ECO:0000269|PubMed:28808133, ECO:0000269|PubMed:8501045}. In the E. coli K-12 strains MG1655 (represented in EcoCyc) and W3110, the rph gene contains a frameshift mutation (rph-1) resulting in a shortened open reading frame. As characterized in strain W3110, Rph is truncated at the C-terminus and lacks the weak poly(A) phosphorylase activity associated with RNase PH. The strains also show a pyrimidine starvation phenotype due to a PyrE deficiency that results from the polar effect of the rph frameshift mutation on the downstream pyrE gene ( and discussed in ). In the absence of the G7459-MONOMER RppH, the rph-1-encoded truncated RNase PH inhibits CPLX0-1382-mediated maturation of certain pre-tRNAs. It is thought that the truncated RNase PH protein creates a steric hindrance and reduces access of RNase P to the pre-tRNA...

## Biological Role

Catalyzes RXN0-6482 (reaction.ecocyc.RXN0-6482), poly(A)-specific ribonuclease (reaction.ecocyc.RXN0-7463), RXN0-7473 (reaction.ecocyc.RXN0-7473), RXN0-7477 (reaction.ecocyc.RXN0-7477), TRNA-NUCLEOTIDYLTRANSFERASE-RXN (reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN). Bound by Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2), phosphate (molecule.ecocyc.Pi).

## Annotation

FUNCTION: This an expressed but non-active exoribonuclease allele (PubMed:8501045). The catalytically inactive protein translated in strain K12 MG1655 inhibits the 5'-processing of primary pre-tRNAs with short (<5 nucleotide) leaders in a dominant-negative effect when RNA pyrophosphohydrolase (rppH) is also inactive; perhaps inactive Rph inhibits interaction with RNase P which is exacerbated when RppH cannot cleave the triphosphate of the primary transcript (PubMed:28808133). {ECO:0000269|PubMed:28808133, ECO:0000269|PubMed:8501045}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6482|reaction.ecocyc.RXN0-6482]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7463|reaction.ecocyc.RXN0-7463]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7473|reaction.ecocyc.RXN0-7473]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7477|reaction.ecocyc.RXN0-7477]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3643|gene.b3643]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CG19`
- `GO:GO:0000049; GO:0000175; GO:0003723; GO:0005829; GO:0009022; GO:0016075; GO:0031125; GO:0042780`

## Notes

Truncated inactive ribonuclease PH (Truncated inactive RNase PH) (Inactive RNase PH) (Truncated RNase PH)
