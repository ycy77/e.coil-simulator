---
entity_id: "protein.P0A8P1"
entity_type: "protein"
name: "aat"
source_database: "UniProt"
source_id: "P0A8P1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aat ycaA b0885 JW0868"
---

# aat

`protein.P0A8P1`

## Static

- Type: `protein`
- Source: `UniProt:P0A8P1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Functions in the N-end rule pathway of protein degradation where it conjugates Leu, Phe and, less efficiently, Met from aminoacyl-tRNAs to the N-termini of proteins containing an N-terminal arginine or lysine. L/F-transferase (Aat) attaches leucine and phenylalanine to exposed amino-terminal arginines and lysines on proteins. This is a key step in the ClpAP-dependent N-end rule degradation pathway. L/F-transferase catalyzes the transfer of leucine and phenylalanine from charged tRNA to amino-terminal lysines and arginines on substrate proteins . When assayed with small peptides, Aat only modifies peptides bearing amino-terminal L-arginine and L-lysine, although the simple dipeptide D-lysyl-D-valine is not a substrate . Testing with purified Aat and actual protein substrates shows that Aat will only transfer to amino-terminal, rather than internal, arginines in proteins . Though addition of both leucine and phenylalanine occurs in vitro, an in vivo experiment with arginine-β-galactosidase yielded only leucine addition . In one case, purified L/F-transferase has been shown to transfer methionine onto the amino-terminus of substrate peptides . L/F-transferase has also been shown to transfer to an unidentified 12 kD protein component of the 30S ribosome...

## Biological Role

Catalyzes L-leucyl-tRNA(Leu):[protein] N-terminal L-lysine leucyltransferase (reaction.R11443), L-leucyl-tRNA(Leu):[protein] N-terminal L-arginine leucyltransferase (reaction.R11444), LEUCYLTRANSFERASE-RXN (reaction.ecocyc.LEUCYLTRANSFERASE-RXN), RXN-17846 (reaction.ecocyc.RXN-17846), RXN-17847 (reaction.ecocyc.RXN-17847), RXN-17848 (reaction.ecocyc.RXN-17848).

## Annotation

FUNCTION: Functions in the N-end rule pathway of protein degradation where it conjugates Leu, Phe and, less efficiently, Met from aminoacyl-tRNAs to the N-termini of proteins containing an N-terminal arginine or lysine.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R11443|reaction.R11443]] `KEGG` `database` - via EC:2.3.2.6
- `catalyzes` --> [[reaction.R11444|reaction.R11444]] `KEGG` `database` - via EC:2.3.2.6
- `catalyzes` --> [[reaction.ecocyc.LEUCYLTRANSFERASE-RXN|reaction.ecocyc.LEUCYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17846|reaction.ecocyc.RXN-17846]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17847|reaction.ecocyc.RXN-17847]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17848|reaction.ecocyc.RXN-17848]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0885|gene.b0885]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8P1`
- `KEGG:ecj:JW0868;eco:b0885;ecoc:C3026_05490;`
- `GeneID:75206174;945490;`
- `GO:GO:0005737; GO:0008914; GO:0016755; GO:0030163`
- `EC:2.3.2.6`

## Notes

Leucyl/phenylalanyl-tRNA--protein transferase (EC 2.3.2.6) (L/F-transferase) (Leucyltransferase) (Phenyalanyltransferase)
