---
entity_id: "protein.P02918"
entity_type: "protein"
name: "mrcA"
source_database: "UniProt"
source_id: "P02918"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:7006606}; Single-pass type II membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mrcA ponA b3396 JW3359"
---

# mrcA

`protein.P02918`

## Static

- Type: `protein`
- Source: `UniProt:P02918`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:7006606}; Single-pass type II membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Cell wall formation. Synthesis of cross-linked peptidoglycan from the lipid intermediates. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a penicillin-sensitive transpeptidase C-terminal domain (cross-linking of the peptide subunits). {ECO:0000269|PubMed:7006606}. PBP1A, the product of the mrcA gene, is a bifunctional peptidoglycan synthase with transglycosylase and transpeptidase activity. PBP1A is implicated in cytoskeleton independent glycan synthesis in E. coli K-12; PBP1A does not exhibit any EG10608-MONOMER MreB-like directional motion . PBP1A is required for maximal fitness in alkaline conditions (pH 6.5-8.2); PBP1A activity is reduced in acidic conditions . Purified PBP1A produces murein with an average length of 20 disaccharide units and with approximately 20% of peptides involved in cross-links; purified PBP1A requires glycan polymers with monomeric peptides for transpeptidation reactions and can integrate newly synthesized glycan chains into existing sacculi . Purified PBP1A catalyses transglycosylation using both disaccharide molecules (Lipid II) and tetrasaccharide molecules ('Lipid IV') as sole substrates; reactions using lipid II are more processive and yield longer glycan chains; reactions using 'lipid IV' proceed using a distributive mechanism (ie...

## Biological Role

Catalyzes R06177 (reaction.R06177), [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase (reaction.R06178), R06179 (reaction.R06179). Component of peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcA (complex.ecocyc.CPLX0-7717).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

FUNCTION: Cell wall formation. Synthesis of cross-linked peptidoglycan from the lipid intermediates. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a penicillin-sensitive transpeptidase C-terminal domain (cross-linking of the peptide subunits). {ECO:0000269|PubMed:7006606}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - via EC:2.4.99.28
- `is_component_of` --> [[complex.ecocyc.CPLX0-7717|complex.ecocyc.CPLX0-7717]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3396|gene.b3396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02918`
- `KEGG:ecj:JW3359;eco:b3396;ecoc:C3026_18425;`
- `GeneID:947907;`
- `GO:GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0008955; GO:0009002; GO:0009252; GO:0030288; GO:0046677; GO:0071555`
- `EC:2.4.99.28; 3.4.16.4`

## Notes

Penicillin-binding protein 1A (PBP-1a) (PBP1a) [Includes: Penicillin-insensitive transglycosylase (EC 2.4.99.28) (Peptidoglycan TGase); Penicillin-sensitive transpeptidase (EC 3.4.16.4) (DD-transpeptidase)]
