---
entity_id: "protein.P09546"
entity_type: "protein"
name: "putA"
source_database: "UniProt"
source_id: "P09546"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "putA poaA b1014 JW0999"
---

# putA

`protein.P09546`

## Static

- Type: `protein`
- Source: `UniProt:P09546`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Oxidizes proline to glutamate for use as a carbon and nitrogen source and also function as a transcriptional repressor of the put operon. PutA is a flavoprotein with mutually exclusive functions as a transcriptional repressor and membrane-associated enzyme. The switch between the two activities is due to conformational changes triggered by the redox state of FAD. In the presence of proline, PutA is associated with the cytoplasmic membrane and acts a bifunctional enzyme catalyzing both reactions of the PROUT-PWY-I pathway: the oxidation of proline by proline dehydrogenase and subsequent oxidation to glutamate by pyrroline-5-carboxylate (P5C) dehydrogenase. The kinetics of the coupled reaction is best described by substrate channeling. In the absence of proline, PutA is cytoplasmic and functions as a transcriptional repressor of the put regulon. The N-terminal 47 residues with a ribbon-helix-helix fold contain the dimerization domain and the specific DNA-binding activity of PutA . The Lys9 residue is essential for recognition of put promoter DNA . Crystal structures of this domain have been solved . In the absence of proline, PutA binds to operator sequences in the putA-putP intergenic region and represses transcription, most likely by keeping RNA polymerase from binding to the putA promoter...

## Biological Role

Catalyzes L-glutamate gamma-semialdehyde:NAD+ oxidoreductase (reaction.R00245), (S)-1-pyrroline-5-carboxylate:NAD+ oxidoreductase (reaction.R00707), (S)-1-pyrroline-5-carboxylate:NADP+ oxidoreductase (reaction.R00708). Component of fused DNA-binding transcriptional repressor / proline dehydrogenase / 1-pyrroline-5-carboxylate dehydrogenase PutA (complex.ecocyc.PUTA-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Oxidizes proline to glutamate for use as a carbon and nitrogen source and also function as a transcriptional repressor of the put operon.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00245|reaction.R00245]] `KEGG` `database` - via EC:1.2.1.88
- `catalyzes` --> [[reaction.R00707|reaction.R00707]] `KEGG` `database` - via EC:1.2.1.88
- `catalyzes` --> [[reaction.R00708|reaction.R00708]] `KEGG` `database` - via EC:1.2.1.88
- `is_component_of` --> [[complex.ecocyc.PUTA-CPLX|complex.ecocyc.PUTA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1014|gene.b1014]] `RegulonDB` `C` - regulator=PutA; target=putA; function=-
- `represses` --> [[gene.b1015|gene.b1015]] `RegulonDB` `C` - regulator=PutA; target=putP; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1014|gene.b1014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09546`
- `KEGG:ecj:JW0999;eco:b1014;ecoc:C3026_06165;`
- `GeneID:945600;`
- `GO:GO:0000987; GO:0001217; GO:0003677; GO:0003842; GO:0004657; GO:0005829; GO:0005886; GO:0006979; GO:0009898; GO:0010133; GO:0042802; GO:0042803; GO:0043565; GO:0045892; GO:0050660`
- `EC:1.2.1.88; 1.5.5.2`

## Notes

Bifunctional protein PutA [Includes: Proline dehydrogenase (EC 1.5.5.2) (Proline oxidase); Delta-1-pyrroline-5-carboxylate dehydrogenase (P5C dehydrogenase) (EC 1.2.1.88) (L-glutamate gamma-semialdehyde dehydrogenase)]
