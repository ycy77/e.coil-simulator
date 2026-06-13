---
entity_id: "protein.P0ACC1"
entity_type: "protein"
name: "prmC"
source_database: "UniProt"
source_id: "P0ACC1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prmC hemK b1212 JW1203"
---

# prmC

`protein.P0ACC1`

## Static

- Type: `protein`
- Source: `UniProt:P0ACC1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Methylates the class 1 translation termination release factors RF1/PrfA and RF2/PrfB on the glutamine residue of the universally conserved GGQ motif, i.e. on 'Gln-235' in RF1 and on 'Gln-252' in RF2. {ECO:0000269|PubMed:11805295, ECO:0000269|PubMed:11847124, ECO:0000269|PubMed:16364916}. PrmC is a protein-(glutamine-N5) methyltransferase that methylates EG10761-MONOMER (RF1) and EG10762-MONOMER at their GGQ motifs . Methylation of these release factors increases termination efficiency . The PrmC/HemK family of proteins shows similarity to the gamma subfamily of S-adenosyl-methionine-dependent adenine-specific DNA methyltransferases . A crystal structure of PrmC is reported at 3.2 Å resolution . The C terminus contains a number of conserved residues surrounding the AdoHcy binding site . The N-terminal domain was suggested to determine methyltransferase substrate specificity and shows structural similarity to a number of protein-interacting domains . The crystal structure of a complex between RF1 and PrmC shows that the N-terminal domain interacts with both the GGQ motif and the central domain of RF1 . The N-terminal domain of PrmC was used as a model substrate to study co-translational protein folding . A mutant shows a defect in nonsense codon recognition and a growth defect that is suppressed by mutations in prfB...

## Biological Role

Catalyzes RXN-14992 (reaction.ecocyc.RXN-14992).

## Annotation

FUNCTION: Methylates the class 1 translation termination release factors RF1/PrfA and RF2/PrfB on the glutamine residue of the universally conserved GGQ motif, i.e. on 'Gln-235' in RF1 and on 'Gln-252' in RF2. {ECO:0000269|PubMed:11805295, ECO:0000269|PubMed:11847124, ECO:0000269|PubMed:16364916}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14992|reaction.ecocyc.RXN-14992]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1212|gene.b1212]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACC1`
- `KEGG:ecj:JW1203;eco:b1212;ecoc:C3026_07120;`
- `GeneID:75171323;945779;`
- `GO:GO:0003676; GO:0006415; GO:0006479; GO:0008276; GO:0008757; GO:0010468; GO:0018364; GO:0036009; GO:0102559`
- `EC:2.1.1.297`

## Notes

Release factor glutamine methyltransferase (RF MTase) (EC 2.1.1.297) (M.EcoKHemKP) (N5-glutamine methyltransferase PrmC) (Protein release factor methylation C) (Protein-(glutamine-N5) MTase PrmC) (Protein-glutamine N-methyltransferase PrmC)
