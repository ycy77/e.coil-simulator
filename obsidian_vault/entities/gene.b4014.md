---
entity_id: "gene.b4014"
entity_type: "gene"
name: "aceB"
source_database: "NCBI RefSeq"
source_id: "gene-b4014"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4014"
  - "aceB"
---

# aceB

`gene.b4014`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4014`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aceB (gene.b4014) is a gene entity. It encodes aceB (protein.P08997). Encoded protein function: Malate synthase A (MSA) (EC 2.3.3.9) EcoCyc product frame: MALATE-SYNTHASE. EcoCyc synonyms: mas. Genomic coordinates: 4215478-4217079. EcoCyc protein note: Malate synthase catalyzes the Claisen condensation of glyoxylate and acetyl-CoA, initially forming a malyl-CoA intermediate that is hydrolyzed to the products malate and CoA. There are two isozymes of malate synthase in E. coli . Malate synthase A is a key enzyme in the GLYOXYLATE-BYPASS. It metabolizes glyoxylate formed in the dissimilation of acetate. The isozyme MALSYNG-MONOMER is responsible for almost all of the malate synthase activity in cells metabolizing glyoxylate formed during growth on glycolate . Malate synthase A catalyzes the irreversible condensation of ACETYL-COA with GLYOX to produce MAL and CO-A. The formation of (S)-malate is a key reaction in the GLYOXYLATE-BYPASS. This cycle is similar to the TCA cycle (see TCA) but it bypasses the TCA cycle reactions that lead to a loss of CARBON-DIOXIDE, thus providing TCA cycle intermediates for cell carbon biosynthesis (see TCA-GLYOX-BYPASS). The glyoxylate cycle has been extensively studied in connection with growth on acetate which is used in the synthesis of these biosynthetic precursors. E. coli malate synthase A has been structurally characterized...

## Biological Role

Repressed by iclR (protein.P16528), nac (protein.Q47005). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), rpoD (protein.P00579), lrp (protein.P0ACJ0), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08997|protein.P08997]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aceB; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=aceB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=aceB; function=+
- `represses` <-- [[protein.P16528|protein.P16528]] `RegulonDB` `S` - regulator=IclR; target=aceB; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=aceB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013125,ECOCYC:EG10023,GeneID:948512`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4215478-4217079:+; feature_type=gene
