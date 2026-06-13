---
entity_id: "protein.P76045"
entity_type: "protein"
name: "ompG"
source_database: "UniProt"
source_id: "P76045"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ompG b1319 JW1312"
---

# ompG

`protein.P76045`

## Static

- Type: `protein`
- Source: `UniProt:P76045`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Forms channels functionally larger than those of classical porins. {ECO:0000269|PubMed:11758943}.; FUNCTION: May act as a regulator of the RCS-phosphorelay signal transduction pathway. {ECO:0000269|PubMed:11758943}. ompG encodes an outer membrane protein (OMP) in E. coli K-12. ompG is not expressed under normal laboratory conditions in many K-12 strains; deletions upstream of ompG which bring it under the control of an unrelated promoter induce expression . When expressed, OmpG functions as a nonspecific outer membrane channel; OmpG produces a larger channel than the classical outer membrane porins (OmpF and OmpC) - in addition to the efficient transport of monosaccharides, OmpG facilitates the diffusion of dissacharides (sucrose) and trisaccharides (raffinose); OmpG appears to function as a monomer; OmpG is predicted to contain 16 transmembrane β strands . OmpG is a monomeric porin . OmpG is a 14-stranded β-barrel porin with short periplasmic turns and seven extracellular loops; crystal structures in two different conformations suggest that extracellular loop 6 may be involved in pH dependent gating of the OmpG channel . When reconstituted into native E. coli lipids, OmpG assembles into both monomers and dimers - both forms exhibit open pore entrances at neutral pH and a closed pore conformation at pH5.0 . OmpG undergoes pH induced conformational change...

## Biological Role

Catalyzes RXN0-2542 (reaction.ecocyc.RXN0-2542).

## Annotation

FUNCTION: Forms channels functionally larger than those of classical porins. {ECO:0000269|PubMed:11758943}.; FUNCTION: May act as a regulator of the RCS-phosphorelay signal transduction pathway. {ECO:0000269|PubMed:11758943}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2542|reaction.ecocyc.RXN0-2542]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1319|gene.b1319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76045`
- `KEGG:ecj:JW1312;eco:b1319;ecoc:C3026_07725;`
- `GeneID:75203434;945889;`
- `GO:GO:0006811; GO:0009279; GO:0015288; GO:0015478; GO:0015481; GO:0034219; GO:0046930`

## Notes

Outer membrane porin G (Outer membrane protein G)
