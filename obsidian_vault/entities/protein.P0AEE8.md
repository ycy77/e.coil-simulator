---
entity_id: "protein.P0AEE8"
entity_type: "protein"
name: "dam"
source_database: "UniProt"
source_id: "P0AEE8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dam b3387 JW3350"
---

# dam

`protein.P0AEE8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEE8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: An alpha subtype methylase that recognizes the double-stranded sequence 5'-GATC-3' and methylates A-2 on both strands (Probable) (PubMed:12654995). Although it shares sequence specificity with a number of type II restriction endonucleases and methylases, it is thought to act in methyl-directed mismatch repair, initiation of chromosome replication and gene expression. Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:36326440, ECO:0000303|PubMed:12654995, ECO:0000305|PubMed:6300769}. DNA adenine methyltransferase (Dam) is responsible for methylation of nearly all GATC sequences in the E. coli genome . Dam activity is involved in methyl-directed mismatch repair, initiation of chromosome replication, and gene expression. The intracellular level of Dam is limiting ; Dam occurs at about 130 molecules per rapidly growing cell . Dam transfers a methyl group from S-adenosyl-L-methionine (AdoMet) to create a N6-methyladenine at the GATC site. This is accomplished by a base-flipping mechanism in which the target residue is flipped out of the DNA strand into the active site of the enzyme . AdoMet can be crosslinked to a peptide corresponding to amino acids 10-14 of Dam...

## Biological Role

Catalyzes 2.1.1.72-RXN (reaction.ecocyc.2.1.1.72-RXN).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: An alpha subtype methylase that recognizes the double-stranded sequence 5'-GATC-3' and methylates A-2 on both strands (Probable) (PubMed:12654995). Although it shares sequence specificity with a number of type II restriction endonucleases and methylases, it is thought to act in methyl-directed mismatch repair, initiation of chromosome replication and gene expression. Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:36326440, ECO:0000303|PubMed:12654995, ECO:0000305|PubMed:6300769}.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.1.1.72-RXN|reaction.ecocyc.2.1.1.72-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3387|gene.b3387]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEE8`
- `KEGG:ecj:JW3350;eco:b3387;ecoc:C3026_18380;`
- `GeneID:75173544;75206325;947893;`
- `GO:GO:0006261; GO:0006298; GO:0009007; GO:0009307; GO:0009411; GO:0032259; GO:0043565; GO:1902328; GO:1904047`
- `EC:2.1.1.72`

## Notes

DNA adenine methylase (EC 2.1.1.72) (DNA adenine methyltransferase) (Deoxyadenosyl-methyltransferase) (Orphan methyltransferase M.EcoKDam) (M.EcoKDam)
