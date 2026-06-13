---
entity_id: "gene.b2061"
entity_type: "gene"
name: "wzb"
source_database: "NCBI RefSeq"
source_id: "gene-b2061"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2061"
  - "wzb"
---

# wzb

`gene.b2061`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2061`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wzb (gene.b2061) is a gene entity. It encodes wzb (protein.P0AAB2). Encoded protein function: FUNCTION: Dephosphorylates Wzc (PubMed:10348860). Required for the extracellular polysaccharide colanic acid synthesis, probably involved in the export of colanic acid from the cell to medium (PubMed:11090276). Involved in protection of cells against contact-dependent growth inhibition (CDI), probably due to the loss of a physical impediment to cell-cell contact. {ECO:0000269|PubMed:10348860, ECO:0000269|PubMed:11090276, ECO:0000269|PubMed:18761695}. EcoCyc product frame: G7106-MONOMER. Genomic coordinates: 2135655-2136098. EcoCyc protein note: Wzb is a protein-tyrosine phosphatase with activity towards autophosphorylated G7105-MONOMER "Wzc" protein . Autophosphorylation of Wzc negatively regulates colanic acid biosynthesis, and Wzb activity counteracts this negative regulation . Wzb acts on the phosphorylated tyrosine residues of the C-terminal tyrosine cluster in Wzc, but has little phosphatase activity toward the phosphorylated Y568 residue in Wzc . Wzb also does not exhibit significant phosphatase activity toward UDP-glucose dehydrogenase, a substrate of the Wzc kinase...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAB2|protein.P0AAB2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=wzb; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=wzb; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wzb; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006822,ECOCYC:G7106,GeneID:946564`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2135655-2136098:-; feature_type=gene
