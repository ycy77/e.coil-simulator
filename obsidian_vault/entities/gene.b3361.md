---
entity_id: "gene.b3361"
entity_type: "gene"
name: "fic"
source_database: "NCBI RefSeq"
source_id: "gene-b3361"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3361"
  - "fic"
---

# fic

`gene.b3361`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3361`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fic (gene.b3361) is a gene entity. It encodes fic (protein.P20605). Encoded protein function: FUNCTION: Probable adenylyltransferase that mediates the addition of adenosine 5'-monophosphate (AMP) to specific residues of target proteins (By similarity). Involved in cell filamentation induced by cyclic AMP. May have some role in cell division. {ECO:0000250}. EcoCyc product frame: EG10307-MONOMER. EcoCyc synonyms: ficT. Genomic coordinates: 3490861-3491463. EcoCyc protein note: The Fic protein is the founding member of a widespread family of proteins. It is related to the phage P1 toxin Doc and contains a sequence motif required for AMPylation activity in related proteins . A EG12374-MONOMER small protein encoded upstream of Fic is homologous to the cognate antitoxins . However, the E. coli Fic belongs to a set of enterobacterial FicT homologs with an altered FIC domain signature motif, where a hydrophobic residue is substituted for a conserved arginine residue that is involved in ATP binding in the FicT proteins with AMP transferase activity . Unlike other FicT proteins, expression of the wild-type E. coli protein does not cause a detectable growth defect . Crystal structures of the Fic-FicA complex have been solved. Combined with phylogenetic analysis, the crystal structures show a conserved potential ligand-binding pocket; the ligand awaits identification...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P20605|protein.P20605]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=fic; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010987,ECOCYC:EG10307,GeneID:947872`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3490861-3491463:-; feature_type=gene
