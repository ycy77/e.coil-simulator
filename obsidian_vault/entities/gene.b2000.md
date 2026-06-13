---
entity_id: "gene.b2000"
entity_type: "gene"
name: "flu"
source_database: "NCBI RefSeq"
source_id: "gene-b2000"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2000"
  - "flu"
---

# flu

`gene.b2000`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2000`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flu (gene.b2000) is a gene entity. It encodes flu (protein.P39180). Encoded protein function: FUNCTION: Controls colony form variation and autoaggregation. May function as an adhesin. {ECO:0000269|PubMed:22466966}. EcoCyc product frame: G7080-MONOMER. EcoCyc synonyms: agn43, yzzX, yeeQ, agn. Genomic coordinates: 2071539-2074658. EcoCyc protein note: agn43 encodes a 1,039 amino acid product with a 52 amino acid N-terminal signal sequence. The mature, peptidase-processed protein is then autocatalytically cleaved to yield two subunits . One is a 60 kDa α43 subunit found peripheral to the outer membrane , extending beyond O-side chains of smooth lipopolysaccharide . The other is a heat modifiable 53 kDa β43 integral membrane protein . Ag43 is an autotransporter as β43 forms an 18 stranded β-barrel through which α43 is translocated . The Ag43 α subunit forms a β-helix structure consisting of 20 rungs, each containing 3 β-strands and 3 turns, which stack in parallel . Both polypeptides are associated with the outer membrane in equal stoichiometry . Immunofluorescence studies of Ag43-producing E. coli showed that the protein is seen evenly distributed over the surface of the entire cell . Based on conserved features, Ag43 can be placed in a group of similar autotransporters that includes AIDA-I and TibA, an adhesin of enterotoxigenic E. coli...

## Biological Role

Repressed by oxyR (protein.P0ACQ4). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39180|protein.P39180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=flu; function=+
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=flu; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006642,ECOCYC:G7080,GeneID:946540`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2071539-2074658:+; feature_type=gene
