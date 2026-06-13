---
entity_id: "protein.P16384"
entity_type: "protein"
name: "miaA"
source_database: "UniProt"
source_id: "P16384"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "miaA trpX b4171 JW4129"
---

# miaA

`protein.P16384`

## Static

- Type: `protein`
- Source: `UniProt:P16384`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of a dimethylallyl group onto the adenine at position 37 in tRNAs that read codons beginning with uridine, leading to the formation of N6-(dimethylallyl)adenosine (i(6)A). {ECO:0000269|PubMed:9012675, ECO:0000269|PubMed:9148919}. Dimethylallyl diphosphate:tRNA dimethylallyltransferase (DMAPP-tRNA transferase, MiaA) catalyzes the first step in the pathway for hypermodification of the A37 base of certain tRNAs such as tRNATyr and tRNAPhe. Further thiomethylation of the A37 position is dependent on the presence of the isopentenyl modification . MiaA transfers the dimethylallyl moiety of DMAPP to the N6 position of A37, which is adjacent to the anticodon . This modification is required for efficient binding of tRNATyr to ribosomes and is important in preventing frameshifts and other mutations . MiaA-catalyzed tRNA modification is involved in regulating the translation efficiency of modification-tunable transcripts (MoTTs) . MiaA can act on isolated tRNA stem-loops, as long as the helix stem and the A36-A37-A38 motif are both present . Co-crystal structures of MiaA in complex with tRNAPhe have been solved, showing a mutually induced fit mechanism of recognition involving structural rearrangement of the anticodon loop of the tRNA . No substantial change in the structure of the catalytic domain of MiaA is seen upon tRNA binding...

## Biological Role

Catalyzes RXN0-6274 (reaction.ecocyc.RXN0-6274). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a dimethylallyl group onto the adenine at position 37 in tRNAs that read codons beginning with uridine, leading to the formation of N6-(dimethylallyl)adenosine (i(6)A). {ECO:0000269|PubMed:9012675, ECO:0000269|PubMed:9148919}.

## Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6274|reaction.ecocyc.RXN0-6274]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4171|gene.b4171]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16384`
- `KEGG:ecj:JW4129;eco:b4171;ecoc:C3026_22540;`
- `GeneID:93777650;948690;`
- `GO:GO:0005524; GO:0006400; GO:0034605; GO:0052381; GO:1990497`
- `EC:2.5.1.75`

## Notes

tRNA dimethylallyltransferase (EC 2.5.1.75) (Dimethylallyl diphosphate:tRNA dimethylallyltransferase) (DMAPP:tRNA dimethylallyltransferase) (DMATase) (Isopentenyl-diphosphate:tRNA isopentenyltransferase) (IPP transferase) (IPPT) (IPTase)
