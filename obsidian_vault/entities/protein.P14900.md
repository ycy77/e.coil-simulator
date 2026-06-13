---
entity_id: "protein.P14900"
entity_type: "protein"
name: "murD"
source_database: "UniProt"
source_id: "P14900"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murD b0088 JW0086"
---

# murD

`protein.P14900`

## Static

- Type: `protein`
- Source: `UniProt:P14900`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Cell wall formation (Probable). Catalyzes the addition of glutamate to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanine (UMA) (PubMed:1765076). {ECO:0000269|PubMed:1765076, ECO:0000305}. UDP-N-acetylmuramoyl-L-alanine:D-glutamate ligase (MurD) catalyzes the addition of the second amino acid to the peptide moiety of the monomer unit of peptidoglycan. There are estimated to be less than 1000 copies of MurD in the cell . Biosynthesis of the cytoplasmic precursor subunit of peptidoglycan has been reconstituted in vitro . The reaction mechanism and specific inhibitors of the enzyme have been studied . In vitro in the absence of D-glutamate, MurD can catalyze the formation of p4A from ATP via an acyl phosphate intermediate . Crystal structures of the enzyme alone and in complex with substrates, product or inhibitors have been solved, and a catalytic mechanism involving an acyl phosphate intermediate was deduced . Results from site-directed mutagenesis of conserved amino acid residues within the active site correlated with their assigned function based on the crystal structures . The K198 residue is present as a carbamate derivative ; the modification is important for catalytic activity . Molecular dynamics (MD) simulations were performed to provide insight into structural changes during substrate binding and transition into the active conformation...

## Biological Role

Catalyzes UDP-NACMURALA-GLU-LIG-RXN (reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cell wall formation (Probable). Catalyzes the addition of glutamate to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanine (UMA) (PubMed:1765076). {ECO:0000269|PubMed:1765076, ECO:0000305}.

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN|reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0088|gene.b0088]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14900`
- `KEGG:ecj:JW0086;eco:b0088;ecoc:C3026_00345;`
- `GeneID:944818;`
- `GO:GO:0005524; GO:0005737; GO:0008360; GO:0008764; GO:0009252; GO:0042802; GO:0051301; GO:0071555`
- `EC:6.3.2.9`

## Notes

UDP-N-acetylmuramoylalanine--D-glutamate ligase (EC 6.3.2.9) (D-glutamic acid-adding enzyme) (UDP-N-acetylmuramoyl-L-alanyl-D-glutamate synthetase)
