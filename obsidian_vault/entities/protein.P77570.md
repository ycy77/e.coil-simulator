---
entity_id: "protein.P77570"
entity_type: "protein"
name: "anmK"
source_database: "UniProt"
source_id: "P77570"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "anmK ydhH b1640 JW1632"
---

# anmK

`protein.P77570`

## Static

- Type: `protein`
- Source: `UniProt:P77570`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the specific phosphorylation of 1,6-anhydro-N-acetylmuramic acid (anhMurNAc) with the simultaneous cleavage of the 1,6-anhydro ring, generating MurNAc-6-P. Is required for the utilization of anhMurNAc either imported from the medium or derived from its own cell wall murein, and thus plays a role in cell wall recycling. {ECO:0000269|PubMed:15901686, ECO:0000269|PubMed:16452451}. AnmK is one of the enzymes responsible for the recycling of murein. Anhydro-N-acetylmuramic acid (anhMurNAc) is produced by the cleavage of muropeptide by NagZ (between the GlcNAc and the anhMurNAc moieties) and AmpD (between the anhMurNAc and peptide moieties), and AnmK catalyzes the hydrolysis of the 1,6-anhydro bond and simultaneous phosphorylation of anhMurNAc to N-acetylmuramate 6-phosphate. An etherase then cleaves the ether bond between the GlcNAc and D-lactate moieties of N-acetylmuramate 6-phosphate . In an anmK null mutant, anhMurNAc does not accumulate inside the cell, although no other enzyme activity that is able to modify anhMurNAc can be detected. When anhMurNAc can not be phosphorylated, it is lost into the medium instead . Review:

## Biological Role

Catalyzes RXN0-4621 (reaction.ecocyc.RXN0-4621). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the specific phosphorylation of 1,6-anhydro-N-acetylmuramic acid (anhMurNAc) with the simultaneous cleavage of the 1,6-anhydro ring, generating MurNAc-6-P. Is required for the utilization of anhMurNAc either imported from the medium or derived from its own cell wall murein, and thus plays a role in cell wall recycling. {ECO:0000269|PubMed:15901686, ECO:0000269|PubMed:16452451}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4621|reaction.ecocyc.RXN0-4621]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1640|gene.b1640]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77570`
- `KEGG:ecj:JW1632;eco:b1640;ecoc:C3026_09420;`
- `GeneID:946810;`
- `GO:GO:0005524; GO:0006040; GO:0009254; GO:0016301; GO:0016773; GO:0097175`
- `EC:2.7.1.170`

## Notes

Anhydro-N-acetylmuramic acid kinase (EC 2.7.1.170) (AnhMurNAc kinase)
