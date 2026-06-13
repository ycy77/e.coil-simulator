---
entity_id: "protein.P0AE18"
entity_type: "protein"
name: "map"
source_database: "UniProt"
source_id: "P0AE18"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "map b0168 JW0163"
---

# map

`protein.P0AE18`

## Static

- Type: `protein`
- Source: `UniProt:P0AE18`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Removes the N-terminal methionine from nascent proteins. The N-terminal methionine is often cleaved when the second residue in the primary sequence is small and uncharged (Met-Ala-, Cys, Gly, Pro, Ser, Thr, or Val). Requires deformylation of the N(alpha)-formylated initiator methionine before it can be hydrolyzed. {ECO:0000255|HAMAP-Rule:MF_01974, ECO:0000269|PubMed:20521764, ECO:0000269|PubMed:3027045}. All known proteins in E. coli use N-formyl methionine (N-fMet) as the first amino acid in a peptide chain. Amino-terminal maturation involves two enzymes, EG11440-MONOMER (PDF) which removes the formyl group, and methionine aminopeptidase (MAP), which catalyzes the removal of the deformylated methionine residue . Oxidation of N-terminal fMet prevents hydrolysis by MAP as determined using bottom-up proteomics . MAP interacts directly with the ribosome at the ribosomal exit tunnel and competes with EG11440-MONOMER for overlapping sites . MAP does not interfere with binding of EG11003-MONOMER trigger factor or SRP-CPLX SRP to translating ribosomes . The activity of MAP is dependent on the identity of the second, third and fourth amino acid residues of the target protein ; the substrate specificity has been analyzed in detail . The most preferred amino acid residue in the position following the fMet is alanine...

## Biological Role

Catalyzes 3.4.11.18-RXN (reaction.ecocyc.3.4.11.18-RXN). Bound by Fe2+ (molecule.C14818).

## Annotation

FUNCTION: Removes the N-terminal methionine from nascent proteins. The N-terminal methionine is often cleaved when the second residue in the primary sequence is small and uncharged (Met-Ala-, Cys, Gly, Pro, Ser, Thr, or Val). Requires deformylation of the N(alpha)-formylated initiator methionine before it can be hydrolyzed. {ECO:0000255|HAMAP-Rule:MF_01974, ECO:0000269|PubMed:20521764, ECO:0000269|PubMed:3027045}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.11.18-RXN|reaction.ecocyc.3.4.11.18-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0168|gene.b0168]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE18`
- `KEGG:ecj:JW0163;eco:b0168;ecoc:C3026_00765;`
- `GeneID:93777257;947882;`
- `GO:GO:0004239; GO:0005829; GO:0006508; GO:0008198; GO:0070006`
- `EC:3.4.11.18`

## Notes

Methionine aminopeptidase (MAP) (MetAP) (EC 3.4.11.18) (Peptidase M)
