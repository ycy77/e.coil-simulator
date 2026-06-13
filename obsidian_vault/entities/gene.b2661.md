---
entity_id: "gene.b2661"
entity_type: "gene"
name: "gabD"
source_database: "NCBI RefSeq"
source_id: "gene-b2661"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2661"
  - "gabD"
---

# gabD

`gene.b2661`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2661`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gabD (gene.b2661) is a gene entity. It encodes gabD (protein.P25526). Encoded protein function: FUNCTION: Catalyzes the NADP(+)-dependent oxidation of succinate semialdehyde to succinate (PubMed:20174634). Thereby functions in a GABA degradation pathway that allows some E.coli strains to utilize GABA as a nitrogen source for growth (PubMed:7011797). Also catalyzes the conversion of glutarate semialdehyde to glutarate, as part of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). {ECO:0000269|PubMed:20174634, ECO:0000269|PubMed:30498244, ECO:0000305|PubMed:7011797}. EcoCyc product frame: SUCCSEMIALDDEHYDROG-MONOMER. Genomic coordinates: 2791273-2792721.

## Biological Role

Repressed by glaR (protein.P37338). Activated by DNA-binding transcriptional regulator PtrR-L-glutamine (complex.ecocyc.CPLX0-10428), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25526|protein.P25526]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-10428|complex.ecocyc.CPLX0-10428]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gabD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gabD; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gabD; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `C` - regulator=GlaR; target=gabD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008758,ECOCYC:EG11329,GeneID:948060`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2791273-2792721:+; feature_type=gene
