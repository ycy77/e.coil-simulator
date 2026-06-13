---
entity_id: "gene.b3752"
entity_type: "gene"
name: "rbsK"
source_database: "NCBI RefSeq"
source_id: "gene-b3752"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3752"
  - "rbsK"
---

# rbsK

`gene.b3752`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3752`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbsK (gene.b3752) is a gene entity. It encodes rbsK (protein.P0A9J6). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of ribose at O-5 in a reaction requiring ATP and magnesium. The resulting D-ribose-5-phosphate can then be used either for sythesis of nucleotides, histidine, and tryptophan, or as a component of the pentose phosphate pathway. {ECO:0000255|HAMAP-Rule:MF_01987, ECO:0000269|PubMed:11563694, ECO:0000269|PubMed:3011794}. EcoCyc product frame: RIBOKIN-MONOMER. Genomic coordinates: 3937294-3938223. EcoCyc protein note: RbsK is a ribokinase that belongs to the ribokinase subfamily of sugar kinases . Crystal structures of ribokinase alone and in ternary complexes have been solved . They suggest an ordered reaction mechanism with a critical role for conformational changes ; monovalent cation binding leads to a conformational change and activation of the enzyme . Ribokinase specifically binds to the α-furanose form of ribose, as shown in the crystal structure and by NMR techniques . The rare codon AGG, encoding the Arg307 and Arg309 residues, together with the inefficient termination codon UGA lead to tagging of 10-25% of newly synthesized molecules of RbsK by the SsrA system . An rbsK mutant can not utilize D-ribose as the sole source of carbon and energy . In an rbsK mutant, D-ribose is able to leak from the cell...

## Biological Role

Repressed by dsrA (gene.b1954), rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9J6|protein.P0A9J6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=rbsK; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=rbsK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012266,ECOCYC:EG10818,GeneID:948260`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3937294-3938223:+; feature_type=gene
