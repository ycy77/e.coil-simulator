---
entity_id: "gene.b0113"
entity_type: "gene"
name: "pdhR"
source_database: "NCBI RefSeq"
source_id: "gene-b0113"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0113"
  - "pdhR"
---

# pdhR

`gene.b0113`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0113`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdhR (gene.b0113) is a gene entity. It encodes pdhR (protein.P0ACL9). Encoded protein function: FUNCTION: Transcriptional repressor for the pyruvate dehydrogenase complex genes aceEF and lpd. EcoCyc product frame: EG11088-MONOMER. EcoCyc synonyms: aceC, genA, yacB. Genomic coordinates: 122092-122856. EcoCyc protein note: PdhR, "pyruvate dehydrogenase complex regulator," regulates genes involved in the pyruvate dehydrogenase complex . Moreover, PdhR participates in positive regulation of fatty acid degradation genes and negative regulation of cell mobility genes. Gas chromatography analysis indicated an increase in free fatty acids in a mutant lacking PdhR . PdhR controls the synthesis of two key enzymes (Ndh and CyoA) in the terminal electron transport system , the enzymes for producing pyruvate and the enzymes involved in the utilization of pyruvate as a substrate . The pdhR deletion mutant enhanced glucose metabolism under oxygen-limited conditions. This mutant strain showed increased activity of the pyruvate dehydrogenase complex and NADH dehydrogenase . Inhibition of pdhR expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic puromycin . Activity of PdhR is controlled by pyruvate. In the absence of this compound, the PdhR regulator binds to its target promoters . This binding is antagonized by pyruvate...

## Biological Role

Repressed by fnr (protein.P0A9E5), pdhR (protein.P0ACL9), cra (protein.P0ACP1), btsR (protein.P0AFT5). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), rpoD (protein.P00579), fnr (protein.P0A9E5), ompR (protein.P0AA16), rpoS (protein.P13445), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACL9|protein.P0ACL9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (10)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=pdhR; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=pdhR; function=-+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=pdhR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=pdhR; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=pdhR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=pdhR; function=-+
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=pdhR; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=pdhR; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=pdhR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000394,ECOCYC:EG11088,GeneID:944827`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:122092-122856:+; feature_type=gene
