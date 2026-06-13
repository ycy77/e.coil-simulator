---
entity_id: "protein.P39099"
entity_type: "protein"
name: "degQ"
source_database: "UniProt"
source_id: "P39099"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8576051}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "degQ hhoA b3234 JW3203"
---

# degQ

`protein.P39099`

## Static

- Type: `protein`
- Source: `UniProt:P39099`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8576051}.

## Enriched Summary

FUNCTION: DegQ could degrade transiently denatured and unfolded proteins which accumulate in the periplasm following stress conditions. DegQ is efficient with Val-Xaa and Ile-Xaa peptide bonds, suggesting a preference for a beta-branched side chain amino acids. Only unfolded proteins devoid of disulfide bonds appear capable to be cleaved, thereby preventing non-specific proteolysis of folded proteins. DegQ can substitute for the periplasmic protease DegP. {ECO:0000269|PubMed:8576051, ECO:0000269|PubMed:8830688}.

## Biological Role

Component of periplasmic serine endoprotease (complex.ecocyc.CPLX0-8187).

## Annotation

FUNCTION: DegQ could degrade transiently denatured and unfolded proteins which accumulate in the periplasm following stress conditions. DegQ is efficient with Val-Xaa and Ile-Xaa peptide bonds, suggesting a preference for a beta-branched side chain amino acids. Only unfolded proteins devoid of disulfide bonds appear capable to be cleaved, thereby preventing non-specific proteolysis of folded proteins. DegQ can substitute for the periplasmic protease DegP. {ECO:0000269|PubMed:8576051, ECO:0000269|PubMed:8830688}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8187|complex.ecocyc.CPLX0-8187]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b3234|gene.b3234]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39099`
- `KEGG:ecj:JW3203;eco:b3234;ecoc:C3026_17595;`
- `GeneID:75173402;947812;`
- `GO:GO:0004252; GO:0006508; GO:0006515; GO:0008233; GO:0042597; GO:0042802; GO:0051603`
- `EC:3.4.21.107`

## Notes

Periplasmic pH-dependent serine endoprotease DegQ (EC 3.4.21.107) (Protease Do)
