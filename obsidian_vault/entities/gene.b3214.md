---
entity_id: "gene.b3214"
entity_type: "gene"
name: "gltF"
source_database: "NCBI RefSeq"
source_id: "gene-b3214"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3214"
  - "gltF"
---

# gltF

`gene.b3214`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3214`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltF (gene.b3214) is a gene entity. It encodes gltF (protein.P28721). Encoded protein function: FUNCTION: Involved in induction of the so-called NTR enzymes in response to nitrogen deprivation, as well as in glutamate biosynthesis. May mediate the glutamate-dependent repression of the GLT operon. EcoCyc product frame: EG11514-MONOMER. EcoCyc synonyms: ossB. Genomic coordinates: 3361176-3361940. EcoCyc protein note: gltF belongs to an operon with genes for the large and small subunits of glutamate synthase, gltB and gltD . The physiological role of GltF in E. coli is currently unknown. Glutamate synthase mutants are unable to grow under low ammonium concentrations or with alternative nitrogen sources due to their glutamate deficiency . Expression of the gltBDF operon is repressed by growth in glutamate as sole nitrogen source , as well as by NAC under conditions of nitrogen limitation . Both Lrp and IHF are involved in transcriptional activation of the gltBDF operon . gltF is repressed by treatment with acivicin . It is induced upon cold shock in a quadruple-csp-deletion strain . Disruption of gltF was shown to prevent induction of nitrogen metabolism genes by Ntr . However, other studies have shown gltF deletion mutants have no nitrogen metabolism defects, and that growth defects of glutamate synthase mutants result only from glutamate deficiency...

## Biological Role

Repressed by argR (protein.P0A6D0), fnr (protein.P0A9E5), crp (protein.P0ACJ8), leuO (protein.P10151), nac (protein.Q47005). Activated by rpoD (protein.P00579), hdfR (protein.P0A8R9), lrp (protein.P0ACJ0), yeiE (protein.P0ACR4), rpoS (protein.P13445), adiY (protein.P33234), glaR (protein.P37338), gadE (protein.P63204), and 1 more.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28721|protein.P28721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (14)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gltF; function=+
- `activates` <-- [[protein.P0A8R9|protein.P0A8R9]] `RegulonDB` `S` - regulator=HdfR; target=gltF; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=gltF; function=+
- `activates` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gltF; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=gltF; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gltF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=gltF; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gltF; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=gltF; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=gltF; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gltF; function=-
- `represses` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=gltF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gltF; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0010549,ECOCYC:EG11514,GeneID:947746`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3361176-3361940:+; feature_type=gene
