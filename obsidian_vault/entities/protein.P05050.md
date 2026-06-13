---
entity_id: "protein.P05050"
entity_type: "protein"
name: "alkB"
source_database: "UniProt"
source_id: "P05050"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alkB aidD b2212 JW2200"
---

# alkB

`protein.P05050`

## Static

- Type: `protein`
- Source: `UniProt:P05050`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dioxygenase that repairs alkylated DNA and RNA containing 3-methylcytosine or 1-methyladenine by oxidative demethylation. Has highest activity towards 3-methylcytosine. Has lower activity towards alkylated DNA containing ethenoadenine, and no detectable activity towards 1-methylguanine or 3-methylthymine. Accepts double-stranded and single-stranded substrates. Requires molecular oxygen, alpha-ketoglutarate and iron. Provides extensive resistance to alkylating agents such as MMS and DMS (SN2 agents), but not to MMNG and MNU (SN1 agents). {ECO:0000269|PubMed:12226668, ECO:0000269|PubMed:12594517, ECO:0000269|PubMed:16482161, ECO:0000269|PubMed:19706517, ECO:0000269|PubMed:20084272, ECO:0000269|PubMed:21068844}. AlkB is an Fe(II)-containing, 2-oxoglutarate-dependent dioxygenase which catalyses the non-mutagenic repair of methyl lesions in DNA and RNA. Purified AlkB is a 2-oxoglutarate and Fe(II) dependent dioxygenase which accurately repairs 1-methyladenine and 3-methylcytosine lesions in DNA (see also ). Purified AlkB accurately repairs 1-methyladenine and 3-methylcytosine in RNA; episomal expression of alkB reactivates methylated RNA phage in vivo (and further )...

## Biological Role

Catalyzes RXN-18737 (reaction.ecocyc.RXN-18737), RXN-18738 (reaction.ecocyc.RXN-18738), RXN-18739 (reaction.ecocyc.RXN-18739), RXN-21233 (reaction.ecocyc.RXN-21233), RXN-21235 (reaction.ecocyc.RXN-21235), RXN-21236 (reaction.ecocyc.RXN-21236), RXN0-7275 (reaction.ecocyc.RXN0-7275), RXN0-7280 (reaction.ecocyc.RXN0-7280), and 2 more. Bound by Fe2+ (molecule.C14818).

## Annotation

FUNCTION: Dioxygenase that repairs alkylated DNA and RNA containing 3-methylcytosine or 1-methyladenine by oxidative demethylation. Has highest activity towards 3-methylcytosine. Has lower activity towards alkylated DNA containing ethenoadenine, and no detectable activity towards 1-methylguanine or 3-methylthymine. Accepts double-stranded and single-stranded substrates. Requires molecular oxygen, alpha-ketoglutarate and iron. Provides extensive resistance to alkylating agents such as MMS and DMS (SN2 agents), but not to MMNG and MNU (SN1 agents). {ECO:0000269|PubMed:12226668, ECO:0000269|PubMed:12594517, ECO:0000269|PubMed:16482161, ECO:0000269|PubMed:19706517, ECO:0000269|PubMed:20084272, ECO:0000269|PubMed:21068844}.

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18738|reaction.ecocyc.RXN-18738]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18739|reaction.ecocyc.RXN-18739]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21233|reaction.ecocyc.RXN-21233]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21235|reaction.ecocyc.RXN-21235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21236|reaction.ecocyc.RXN-21236]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7275|reaction.ecocyc.RXN0-7275]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7280|reaction.ecocyc.RXN0-7280]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7484|reaction.ecocyc.RXN0-7484]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-986|reaction.ecocyc.RXN0-986]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2212|gene.b2212]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05050`
- `KEGG:ecj:JW2200;eco:b2212;ecoc:C3026_12360;`
- `GeneID:946708;`
- `GO:GO:0005737; GO:0005829; GO:0006281; GO:0006307; GO:0008198; GO:0035513; GO:0035515; GO:0035516; GO:0042245; GO:0051213; GO:0070989; GO:0072702`
- `EC:1.14.11.33`

## Notes

Alpha-ketoglutarate-dependent dioxygenase AlkB (EC 1.14.11.33) (Alkylated DNA repair protein AlkB) (DNA oxidative demethylase AlkB)
