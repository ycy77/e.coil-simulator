---
entity_id: "protein.Q46925"
entity_type: "protein"
name: "csdA"
source_database: "UniProt"
source_id: "Q46925"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csdA ygdJ b2810 JW2781"
---

# csdA

`protein.Q46925`

## Static

- Type: `protein`
- Source: `UniProt:Q46925`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the removal of elemental sulfur and selenium atoms from L-cysteine, L-cystine, L-selenocysteine, and L-selenocystine to produce L-alanine, and transiently retains the released sulfur atom on a cysteine residue, in the form of a persulfide. Can also desulfinate L-cysteine sulfinate (3-sulfino-L-alanine), which is the best substrate of the enzyme. Functions as a selenium delivery protein in the pathway for the biosynthesis of selenophosphate. Seems to participate in Fe/S biogenesis by recruiting the SufBCD-SufE proteins. Transfers sulfur to CsdE that increases the cysteine desulfurase activity of CsdA. Can also transfer sulfur directly to TcdA/CsdL in vitro. Appears to support the function of TcdA in the generation of cyclic threonylcarbamoyladenosine at position 37 (ct(6)A37) in tRNAs that read codons beginning with adenine. {ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:15901727, ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255, ECO:0000269|PubMed:9278392}.

## Biological Role

Component of cysteine sulfinate desulfinase (complex.ecocyc.CPLX0-7838).

## Annotation

FUNCTION: Catalyzes the removal of elemental sulfur and selenium atoms from L-cysteine, L-cystine, L-selenocysteine, and L-selenocystine to produce L-alanine, and transiently retains the released sulfur atom on a cysteine residue, in the form of a persulfide. Can also desulfinate L-cysteine sulfinate (3-sulfino-L-alanine), which is the best substrate of the enzyme. Functions as a selenium delivery protein in the pathway for the biosynthesis of selenophosphate. Seems to participate in Fe/S biogenesis by recruiting the SufBCD-SufE proteins. Transfers sulfur to CsdE that increases the cysteine desulfurase activity of CsdA. Can also transfer sulfur directly to TcdA/CsdL in vitro. Appears to support the function of TcdA in the generation of cyclic threonylcarbamoyladenosine at position 37 (ct(6)A37) in tRNAs that read codons beginning with adenine. {ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:15901727, ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255, ECO:0000269|PubMed:9278392}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7838|complex.ecocyc.CPLX0-7838]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2810|gene.b2810]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46925`
- `KEGG:ecj:JW2781;eco:b2810;ecoc:C3026_15445;`
- `GeneID:947275;`
- `GO:GO:0000096; GO:0006534; GO:0008826; GO:0009000; GO:0016226; GO:0016261; GO:0016783; GO:0016787; GO:0019448; GO:0030170; GO:0031071; GO:0072348; GO:1990221`
- `EC:2.8.1.7; 3.13.1.-; 4.4.1.16`

## Notes

Cysteine desulfurase CsdA (EC 2.8.1.7) (Cysteine sulfinate desulfinase) (CSD) (EC 3.13.1.-) (Selenocysteine lyase) (EC 4.4.1.16)
