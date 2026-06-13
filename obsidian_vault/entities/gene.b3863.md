---
entity_id: "gene.b3863"
entity_type: "gene"
name: "polA"
source_database: "NCBI RefSeq"
source_id: "gene-b3863"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3863"
  - "polA"
---

# polA

`gene.b3863`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3863`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

polA (gene.b3863) is a gene entity. It encodes polA (protein.P00582). Encoded protein function: FUNCTION: In addition to polymerase activity, this DNA polymerase exhibits 3'-5' and 5'-3' exonuclease activity. It is able to utilize nicked circular duplex DNA as a template and can unwind the parental DNA strand from its template.; FUNCTION: Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair. {ECO:0000269|PubMed:36326440}. EcoCyc product frame: EG10746-MONOMER. EcoCyc synonyms: resA. Genomic coordinates: 4046966-4049752. EcoCyc protein note: DNA Polymerase I (Pol I) is a multifunctional enzyme that combines a DNA polymerase activity, "flap-directed" 5' nuclease activity, and a 3' to 5' proofreading exonuclease activity. It is required for several types of DNA repair and is the primary enzyme responsible for Okazaki fragment maturation, i.e. removing RNA primers from newly-synthesized DNA and replacing them with DNA. Pol I is involved in several DNA repair pathways. It is required for excision repair, displacing the UvrABC nuclease and patching the gap it leaves behind . Pol I is also required in MutHLS-mediated very short patch repair . Pol I can excise and replace pyrimidine dimers directly...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by dnaA (protein.P03004).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00582|protein.P00582]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=polA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=polA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012618,ECOCYC:EG10746,GeneID:948356`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4046966-4049752:+; feature_type=gene
