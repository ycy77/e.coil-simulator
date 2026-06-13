---
entity_id: "protein.P0A7J0"
entity_type: "protein"
name: "ribB"
source_database: "UniProt"
source_id: "P0A7J0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ribB htrP b3041 JW3009"
---

# ribB

`protein.P0A7J0`

## Static

- Type: `protein`
- Source: `UniProt:P0A7J0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of D-ribulose 5-phosphate to formate and 3,4-dihydroxy-2-butanone 4-phosphate. {ECO:0000269|PubMed:1597419}. RibB catalyzes the synthesis of the 4-carbon compound DIHYDROXY-BUTANONE-P (3,4-dihydroxy-2-butanone 4-phosphate), a precursor of the terminal intermediate DIMETHYL-D-RIBITYL-LUMAZINE in the biosynthesis of RIBOFLAVIN . ribB is an essential gene . The enzyme is a homodimer in solution . Crystal structures have been solved at 1.55 and 1.4 Å resolution, and various amino acid residues were assigned proposed roles in catalysis and enzyme structure . A solution structure of the enzyme allowed identification of the substrate binding site, residues involved in catalysis, and identification of the Mg2+ binding site . RibB production is induced by low pH, but not by acetate and is regulated by an FMN-sensitive riboswitch that operates both on the transcriptional as well as the translational level . When FMN is abundant, the ribB's rut (Rho utilization) site is open to allow efficient binding of the CPLX0-2441, leading to transcription attenuaton of the downstream ribB gene and as a result, of riboflavin synthesis. When FMN is scarce, the rut site is closed, forming a hairpin structure and impeding Rho binding, resulting in transcription of the gene...

## Biological Role

Catalyzes D-ribulose 5-phosphate formate-lyase (L-3,4-dihydroxybutan-2-one 4-phosphate-forming) (reaction.R07281). Component of 3,4-dihydroxy-2-butanone-4-phosphate synthase (complex.ecocyc.DIOHBUTANONEPSYN-CPLX).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of D-ribulose 5-phosphate to formate and 3,4-dihydroxy-2-butanone 4-phosphate. {ECO:0000269|PubMed:1597419}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07281|reaction.R07281]] `KEGG` `database` - via EC:4.1.99.12
- `is_component_of` --> [[complex.ecocyc.DIOHBUTANONEPSYN-CPLX|complex.ecocyc.DIOHBUTANONEPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3041|gene.b3041]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7J0`
- `KEGG:ecj:JW3009;eco:b3041;ecoc:C3026_16610;`
- `GeneID:93778953;947526;`
- `GO:GO:0000287; GO:0005829; GO:0005886; GO:0008686; GO:0009231; GO:0030145; GO:0042802; GO:0042803`
- `EC:4.1.99.12`

## Notes

3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (DHBPS) (EC 4.1.99.12)
