---
entity_id: "protein.P20605"
entity_type: "protein"
name: "fic"
source_database: "UniProt"
source_id: "P20605"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fic b3361 JW3324"
---

# fic

`protein.P20605`

## Static

- Type: `protein`
- Source: `UniProt:P20605`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable adenylyltransferase that mediates the addition of adenosine 5'-monophosphate (AMP) to specific residues of target proteins (By similarity). Involved in cell filamentation induced by cyclic AMP. May have some role in cell division. {ECO:0000250}. The Fic protein is the founding member of a widespread family of proteins. It is related to the phage P1 toxin Doc and contains a sequence motif required for AMPylation activity in related proteins . A EG12374-MONOMER small protein encoded upstream of Fic is homologous to the cognate antitoxins . However, the E. coli Fic belongs to a set of enterobacterial FicT homologs with an altered FIC domain signature motif, where a hydrophobic residue is substituted for a conserved arginine residue that is involved in ATP binding in the FicT proteins with AMP transferase activity . Unlike other FicT proteins, expression of the wild-type E. coli protein does not cause a detectable growth defect . Crystal structures of the Fic-FicA complex have been solved. Combined with phylogenetic analysis, the crystal structures show a conserved potential ligand-binding pocket; the ligand awaits identification . A strain containing the fic-1 allele, which encodes a G55R change , exhibits heat-sensitive CRP-dependent cell filamentation in the presence of cAMP...

## Biological Role

Component of FicT-FicA complex (complex.ecocyc.CPLX0-8227).

## Annotation

FUNCTION: Probable adenylyltransferase that mediates the addition of adenosine 5'-monophosphate (AMP) to specific residues of target proteins (By similarity). Involved in cell filamentation induced by cyclic AMP. May have some role in cell division. {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8227|complex.ecocyc.CPLX0-8227]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3361|gene.b3361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P20605`
- `KEGG:ecj:JW3324;eco:b3361;ecoc:C3026_18255;`
- `GeneID:75173519;947872;`
- `GO:GO:0005524; GO:0051302; GO:0070733`
- `EC:2.7.7.108`

## Notes

Probable protein adenylyltransferase Fic (EC 2.7.7.108) (Cell filamentation protein Fic)
