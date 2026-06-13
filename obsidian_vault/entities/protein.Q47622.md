---
entity_id: "protein.Q47622"
entity_type: "protein"
name: "sapA"
source_database: "UniProt"
source_id: "Q47622"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sapA b1294 JW1287"
---

# sapA

`protein.Q47622`

## Static

- Type: `protein`
- Source: `UniProt:Q47622`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Not part of a putrescine export system (PubMed:27803167). Very similar to a S.typhimurium protein implicated in antimicrobial peptide resistance, but the SapBCDF operon in E.coli is implicated in putrescine export (PubMed:27803167). {ECO:0000269|PubMed:27803167}. SapA is the periplasmic binding protein of an ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as AMPs, dipeptides and heme . 'Sap family' transporters are widely present in Gram-negative pathogens where they contribute to resistance against antimicrobial peptides (AMPs) (see ). E. coli K-12 contains a 'consensus' sap operon (sapABCDF) encoding all five Sap components (a substrate binding protein, two membrane proteins and two ATP-binding proteins) in tandem . SapA contains two intramolecular disulfide bonds that contribute to the structural integrity of the protein; purified SapA interacts with Heme-b and with the cationic AMP, Protamines protamine . Separately, in E. coli K-12, CPLX0-13226 SapBCDF (but not SapA) has been implicated in putrescine export . The concentration of putrescine in the culture supernatant of a ΔsapA strain is not significantly different compared to wild type . SapA is implicated in uptake of the natural product antibiotic CPD-28147 .

## Biological Role

Component of putative antimicrobial peptide ABC transporter (complex.ecocyc.ABC-29-CPLX).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Not part of a putrescine export system (PubMed:27803167). Very similar to a S.typhimurium protein implicated in antimicrobial peptide resistance, but the SapBCDF operon in E.coli is implicated in putrescine export (PubMed:27803167). {ECO:0000269|PubMed:27803167}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-29-CPLX|complex.ecocyc.ABC-29-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1294|gene.b1294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47622`
- `KEGG:ecj:JW1287;eco:b1294;ecoc:C3026_07595;`
- `GeneID:945873;`
- `GO:GO:0015833; GO:0016020; GO:0030288; GO:0055052; GO:1904680`

## Notes

Probable ABC transporter periplasmic-binding protein SapA
