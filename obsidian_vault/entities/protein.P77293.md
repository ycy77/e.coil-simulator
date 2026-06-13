---
entity_id: "protein.P77293"
entity_type: "protein"
name: "yfdH"
source_database: "UniProt"
source_id: "P77293"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfdH b2351 JW2347"
---

# yfdH

`protein.P77293`

## Static

- Type: `protein`
- Source: `UniProt:P77293`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in O antigen modification. Catalyzes the transfer of the glucose residue from UDP-glucose to a lipid carrier (By similarity). {ECO:0000250}. yfdG, yfdH and yfdI constitute a three gene cluster within the CPS-53/KpLE1 cryptic prophage . yfdG and yfdH show significant homology with the gtrAtype and gtrBtype genes respectively, of the O antigen glucosylation gene cluster in the serotype converting bacteriophages, SfI, SfII, SfX and SfV of Shigella flexneri ; yfdG, yfdH and yfdI show significant homology with the type IV O antigen modification genes (gtrAIV, gtrBIV and gtrIV) in the genome of Shigella flexneri NCTC 8296 . yfdG, yfdH and yfdI mediate partial O-antigen modification when introduced together into S. flexneri serotype Y strain SFL124; yfdG, yfdH and gtrX (from the bacteriphage SfX) confer complete conversion to serotype X when introduced together into S. flexneri serotype Y strain SFL124 . gtrB from Shigella flexneri bacteriophage SfX encodes a bactoprenol glucose transferase . YfdH is predicted to be an inner membrane protein with two transmembrane helices; experimental topology analysis suggests the C terminus is located in the cytoplasm . Please note: E. coli K-12 does not produce an O-antigen due to mutations in the rfb region; a reconstructed strain with all rfb genes intact produces an O16 antigen .

## Biological Role

Catalyzes 2.4.1.78-RXN (reaction.ecocyc.2.4.1.78-RXN).

## Annotation

FUNCTION: Involved in O antigen modification. Catalyzes the transfer of the glucose residue from UDP-glucose to a lipid carrier (By similarity). {ECO:0000250}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.4.1.78-RXN|reaction.ecocyc.2.4.1.78-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2351|gene.b2351]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77293`
- `KEGG:ecj:JW2347;eco:b2351;ecoc:C3026_13080;`
- `GeneID:949098;`
- `GO:GO:0005886; GO:0016757`
- `EC:2.4.1.-`

## Notes

Prophage bactoprenol glucosyl transferase homolog (EC 2.4.1.-) (Bactoprenol glucosyl transferase homolog from prophage CPS-53)
