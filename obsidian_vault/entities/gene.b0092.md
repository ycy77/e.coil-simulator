---
entity_id: "gene.b0092"
entity_type: "gene"
name: "ddlB"
source_database: "NCBI RefSeq"
source_id: "gene-b0092"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0092"
  - "ddlB"
---

# ddlB

`gene.b0092`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0092`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ddlB (gene.b0092) is a gene entity. It encodes ddlB (protein.P07862). Encoded protein function: FUNCTION: Cell wall formation. EcoCyc product frame: DALADALALIGB-MONOMER. EcoCyc synonyms: ddl. Genomic coordinates: 102233-103153. EcoCyc protein note: DdlB is one of two D-alanine—D-alanine ligases in E. coli . D-alanine—D-alanine ligase, along with alanine racemase, makes up the D-alanine branch of peptidoglycan biosynthesis. The enzyme combines two molecules of D-alanine to form D-alanyl-D-alanine, which is then added to the growing cell wall precursor. DdlB belongs to the ATP grasp superfamily. The enzyme is similar to VanA, a DD-ligase with modified substrate specificity that occurs in vancomycin-resistant enterococci . D-alanine—D-alanine ligase is an antibacterial drug target; it has long known to be the target of D-cycloserine . Structural and functional studues revealed that it is the phosphorylated form of D-cycloserine that inhibits DdlB . Crystal structures of DdlB have been solved, and a reaction mechanism was proposed . Kinetic analysis of mutants in predicted active site residues has allowed confirmation and refinement of the proposed reaction mechanism . The reaction involves rapid formation of an enzyme-bound D-alanyl phosphate intermediate...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07862|protein.P07862]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ddlB; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ddlB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000326,ECOCYC:EG10214,GeneID:946324`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:102233-103153:+; feature_type=gene
