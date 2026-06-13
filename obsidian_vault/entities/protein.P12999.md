---
entity_id: "protein.P12999"
entity_type: "protein"
name: "bioC"
source_database: "UniProt"
source_id: "P12999"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioC b0777 JW0760"
---

# bioC

`protein.P12999`

## Static

- Type: `protein`
- Source: `UniProt:P12999`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts the free carboxyl group of a malonyl-thioester to its methyl ester by transfer of a methyl group from S-adenosyl-L-methionine (SAM). It allows to synthesize pimeloyl-ACP via the fatty acid synthetic pathway. E.coli employs a methylation and demethylation strategy to allow elongation of a temporarily disguised malonate moiety to a pimelate moiety by the fatty acid synthetic enzymes. {ECO:0000269|PubMed:20693992, ECO:0000269|PubMed:4864413}. BioC is a methyltransferase involved in an early step of biotin biosynthesis . It is thought to methylate the ω-carboxyl group of MALONYL-ACP "malonyl-[acp]" to form Malonyl-acp-methyl-ester, which is recognized by the fatty acid synthetic enzymes . The methyl ester is processed via the fatty acid elongation cycle to give Pimeloyl-ACP-methyl-esters, which is processed into Pimeloyl-ACPs "pimelyl-[acp]" by EG10122-MONOMER "BioH" . For a long time, neither the exact function of BioC nor the path to pimelate was understood. Lemoine et al. () proposed that BioC may catalyze the stepwise condensation of malonyl-CoA by addition of acetate units. cites unpublished results showing lack of growth of a bioC mutant on pimelate, but 13C tracing indicated that pimelate is not a precursor of biotin . The function of BioC was finally suggested in a 2010 study . Due to difficulties studying the E...

## Biological Role

Catalyzes RXN-11475 (reaction.ecocyc.RXN-11475).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Converts the free carboxyl group of a malonyl-thioester to its methyl ester by transfer of a methyl group from S-adenosyl-L-methionine (SAM). It allows to synthesize pimeloyl-ACP via the fatty acid synthetic pathway. E.coli employs a methylation and demethylation strategy to allow elongation of a temporarily disguised malonate moiety to a pimelate moiety by the fatty acid synthetic enzymes. {ECO:0000269|PubMed:20693992, ECO:0000269|PubMed:4864413}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11475|reaction.ecocyc.RXN-11475]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0777|gene.b0777]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12999`
- `KEGG:ecj:JW0760;eco:b0777;ecoc:C3026_04935;`
- `GeneID:945388;`
- `GO:GO:0008168; GO:0008757; GO:0009102; GO:0010340; GO:0032259; GO:0102130`
- `EC:2.1.1.197`

## Notes

Malonyl-[acyl-carrier protein] O-methyltransferase (Malonyl-ACP O-methyltransferase) (EC 2.1.1.197) (Biotin synthesis protein BioC)
