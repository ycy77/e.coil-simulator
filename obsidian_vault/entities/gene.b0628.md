---
entity_id: "gene.b0628"
entity_type: "gene"
name: "lipA"
source_database: "NCBI RefSeq"
source_id: "gene-b0628"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0628"
  - "lipA"
---

# lipA

`gene.b0628`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0628`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lipA (gene.b0628) is a gene entity. It encodes lipA (protein.P60716). Encoded protein function: FUNCTION: Catalyzes the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to the lipoyl domains of lipoate-dependent enzymes, thereby converting the octanoylated domains into lipoylated derivatives. Free octanoate is not a substrate for LipA. {ECO:0000269|PubMed:11106496, ECO:0000269|PubMed:14700636, ECO:0000269|PubMed:15157071}. EcoCyc product frame: EG11306-MONOMER. EcoCyc synonyms: lip. Genomic coordinates: 659251-660216. EcoCyc protein note: Lipoate synthase catalyzes the final step of de novo lipoate biosynthesis, the insertion of sulfur into the octanoyl side chain of an octanoylated E2 domain to form the lipoate moiety . Lipoate modification of the E2 subunits is important for the function of PYRUVATEDEH-CPLX , 2OXOGLUTARATEDEH-CPLX "α-ketoglutarate dehydrogenase" , and the GCVMULTI-CPLX . Lipoate synthase is a homodimer containing iron-sulfur clusters . Coexpression with the isc operon increases the yield of overexpressed soluble LipA . LipA belongs to the radical SAM superfamily of enzymes . The enzyme uses octanoyl side chains (but not free octanoate) as substrate . The 5'-dA· radicals, generated from SAM, act directly on the octanoyl substrate...

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60716|protein.P60716]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002155,ECOCYC:EG11306,GeneID:945227`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:659251-660216:-; feature_type=gene
