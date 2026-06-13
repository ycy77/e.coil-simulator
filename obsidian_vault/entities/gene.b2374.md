---
entity_id: "gene.b2374"
entity_type: "gene"
name: "frc"
source_database: "NCBI RefSeq"
source_id: "gene-b2374"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2374"
  - "frc"
---

# frc

`gene.b2374`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2374`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frc (gene.b2374) is a gene entity. It encodes frc (protein.P69902). Encoded protein function: FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH via the induction of the oxalate-dependent acid tolerance response (ATR). Catalyzes the transfer of the CoA moiety from formyl-CoA to oxalate. It can also use succinate as an acceptor. {ECO:0000269|PubMed:12844490, ECO:0000269|PubMed:18245280, ECO:0000269|PubMed:23335415}. EcoCyc product frame: G7237-MONOMER. EcoCyc synonyms: yfdW. Genomic coordinates: 2492004-2493254. EcoCyc protein note: YfdW (Frc) is a formyl-CoA transferase with sequence and structural similarity to Frc from Oxalobacter formigenes, a strictly anaerobic bacterium found in the mammalian gut . Unlike the O. formigenes enzyme, the E. coli enzyme shows high substrate specificity . Crystal structures of apo-YfdW and YfdW with CoA, acetyl-CoA, or both acetyl-CoA and oxalate have been solved. YfdW is a homodimer; the ring-shaped monomers are concatenated like links of a chain . The enzymatic reaction mechanism is predicted by structural similarity to related enzymes; residue D169 is predicted to catalyze the reaction . Biochemical data indicates that the kinetic mechanism is ordered bi-bi sequential . Frc is required during the adaption phase of an oxalate-induced acid tolerance response...

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), evgA (protein.P0ACZ4).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69902|protein.P69902]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=frc; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007828,ECOCYC:G7237,GeneID:946842`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2492004-2493254:-; feature_type=gene
