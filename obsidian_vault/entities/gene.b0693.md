---
entity_id: "gene.b0693"
entity_type: "gene"
name: "speF"
source_database: "NCBI RefSeq"
source_id: "gene-b0693"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0693"
  - "speF"
---

# speF

`gene.b0693`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0693`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speF (gene.b0693) is a gene entity. It encodes speF (protein.P24169). Encoded protein function: FUNCTION: The first enzyme leading to putrescine and thus polyamine synthesis. {ECO:0000305}. EcoCyc product frame: ORNDECARBOXDEG-MONOMER. Genomic coordinates: 718262-720460. EcoCyc protein note: E. coli encodes two ornithine decarboxylase enzymes, the biosynthetic (constitutive) ORNDECARBOX-BIO-CPLX SpeC and the degradative (inducible) SpeF . SpeF is activated by the guanosine nucleotides GTP, GDP, pppGpp and ppGpp . SpeF enzymatic activity is induced by growth at low pH (5.5) . SpeF is overproduced from a speF-containing plasmid when cells are grown at pH 5.2, but not at pH 7 . Overexpression of RNase III from a plasmid increases expression from the speF promoter, perhaps by processing of the 5' UTR . Expression of SpeF is also regulated by attenuation in response to ornithine ; see the summary for the MONOMER0-4532.

## Biological Role

Repressed by ompR (protein.P0AA16).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24169|protein.P24169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=speF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002362,ECOCYC:EG10964,GeneID:945297`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:718262-720460:-; feature_type=gene
