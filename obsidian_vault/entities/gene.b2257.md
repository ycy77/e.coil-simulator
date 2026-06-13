---
entity_id: "gene.b2257"
entity_type: "gene"
name: "arnT"
source_database: "NCBI RefSeq"
source_id: "gene-b2257"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2257"
  - "arnT"
---

# arnT

`gene.b2257`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2257`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnT (gene.b2257) is a gene entity. It encodes arnT (protein.P76473). Encoded protein function: FUNCTION: Catalyzes the transfer of the L-Ara4N moiety of the glycolipid undecaprenyl phosphate-alpha-L-Ara4N to lipid A. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11535604}. EcoCyc product frame: G7170-MONOMER. EcoCyc synonyms: yfbI, pmrK. Genomic coordinates: 2370908-2372560. EcoCyc protein note: ArnT is a transferase that catalyzes the addition of 4-AMINO-4-DEOXY-L-ARABINOSE (L-Ara4N) residues from CPD0-1189 to lipid A. This modification confers on the organism resistance to Polymyxins "polymyxin antibiotics" (similar to the effect of lipid A modification by PHOSPHORYL-ETHANOLAMINE, which is catalyzed by EG11613-MONOMER). It should be noted that K-12 derived strains express ArnT, but do not synthesize CPD0-1189 under normal conditions, and thus are sensitive to polymyxin. The enzyme from E. coli has not been studied much, but the Salmonella typhimurium enzyme has been purified and characterized . It has been suggested, although not proven, that the enzyme is involved not only in the attachment of L-Ara4N to lipid A but also in the transport of L-Ara4N from the cytoplasm, where it is synthesized, to the periplasmic side of the inner membrane, where the attachment takes place...

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76473|protein.P76473]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007464,ECOCYC:G7170,GeneID:947297`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2370908-2372560:+; feature_type=gene
