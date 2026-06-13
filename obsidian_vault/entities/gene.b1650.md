---
entity_id: "gene.b1650"
entity_type: "gene"
name: "nemA"
source_database: "NCBI RefSeq"
source_id: "gene-b1650"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1650"
  - "nemA"
---

# nemA

`gene.b1650`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1650`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nemA (gene.b1650) is a gene entity. It encodes nemA (protein.P77258). Encoded protein function: FUNCTION: Involved in the degradation of toxic compounds (PubMed:15184158, PubMed:17504490, PubMed:23506073, PubMed:23527133, PubMed:23536188, PubMed:9013822). Can use a variety of substrates, including the nitrate ester explosives glycerol trinitrate (GTN) and pentaerythritol tetranitrate (PETN), chromate and various electrophiles such as quinones (PubMed:15184158, PubMed:23506073, PubMed:23527133). Involved in resistance to hypochlorous acid (HOCl), which is the active component of household bleach and a powerful antimicrobial during the innate immune response (PubMed:23536188). Catalyzes the reduction of N-ethylmaleimide (NEM) to N-ethylsuccinimide (PubMed:23506073, PubMed:9013822). Together with NfsA and NfsB, can use the nitroaromatic explosive 2,4,6-trinitrotoluene (TNT) (PubMed:17504490). {ECO:0000269|PubMed:15184158, ECO:0000269|PubMed:17504490, ECO:0000269|PubMed:23506073, ECO:0000269|PubMed:23527133, ECO:0000269|PubMed:23536188, ECO:0000269|PubMed:9013822}. EcoCyc product frame: G6890-MONOMER. EcoCyc synonyms: ydhN. Genomic coordinates: 1726659-1727756. EcoCyc protein note: N-ethylmaleimide reductase (NemA) is a member of the "old yellow enzyme" family of flavoproteins and catalyzes the reduction of N-ethylmaleimide (NEM) to N-ethylsuccinimide...

## Biological Role

Repressed by rutR (protein.P0ACU2), nemR (protein.P67430). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77258|protein.P77258]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nemA; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `S` - regulator=RutR; target=nemA; function=-
- `represses` <-- [[protein.P67430|protein.P67430]] `RegulonDB` `S` - regulator=NemR; target=nemA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005516,ECOCYC:G6890,GeneID:946164`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1726659-1727756:+; feature_type=gene
