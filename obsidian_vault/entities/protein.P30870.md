---
entity_id: "protein.P30870"
entity_type: "protein"
name: "glnE"
source_database: "UniProt"
source_id: "P30870"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnE b3053 JW3025"
---

# glnE

`protein.P30870`

## Static

- Type: `protein`
- Source: `UniProt:P30870`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the regulation of glutamine synthetase GlnA, a key enzyme in the process to assimilate ammonia (PubMed:8412694). When cellular nitrogen levels are high, the C-terminal adenylyl transferase inactivates GlnA by covalent transfer of an adenylyl group from ATP to 'Tyr-398' of GlnA, thus reducing its activity (PubMed:4920894, PubMed:9312015). Conversely, when nitrogen levels are low, the N-terminal adenylyl removase (AR) activates GlnA by removing the adenylyl group by phosphorolysis, increasing its activity (PubMed:14766310, PubMed:4893578, PubMed:4920873, PubMed:4934180, PubMed:9312015). The regulatory region of GlnE binds the signal transduction protein PII (GlnB) which indicates the nitrogen status of the cell (PubMed:8412694). {ECO:0000269|PubMed:14766310, ECO:0000269|PubMed:4867671, ECO:0000269|PubMed:4893578, ECO:0000269|PubMed:4920873, ECO:0000269|PubMed:4920894, ECO:0000269|PubMed:4934180, ECO:0000269|PubMed:8412694, ECO:0000269|PubMed:9312015}. glnE encodes a bifunctional polypeptide having both glutamine synthetase adenylyltransferase (ATase) activity and glutamine synthetase deadenylase activity (ATd). It is believed that there are two separate catalytic sites on the polypeptide . GlnE catalyzes the ATP-dependent addition of AMP to a subunit of GLUTAMINESYN-OLIGOMER "glutamine synthetase", with the release of PPi...

## Biological Role

Catalyzes GSADENYLATION-RXN (reaction.ecocyc.GSADENYLATION-RXN), GSDEADENYLATION-RXN (reaction.ecocyc.GSDEADENYLATION-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Involved in the regulation of glutamine synthetase GlnA, a key enzyme in the process to assimilate ammonia (PubMed:8412694). When cellular nitrogen levels are high, the C-terminal adenylyl transferase inactivates GlnA by covalent transfer of an adenylyl group from ATP to 'Tyr-398' of GlnA, thus reducing its activity (PubMed:4920894, PubMed:9312015). Conversely, when nitrogen levels are low, the N-terminal adenylyl removase (AR) activates GlnA by removing the adenylyl group by phosphorolysis, increasing its activity (PubMed:14766310, PubMed:4893578, PubMed:4920873, PubMed:4934180, PubMed:9312015). The regulatory region of GlnE binds the signal transduction protein PII (GlnB) which indicates the nitrogen status of the cell (PubMed:8412694). {ECO:0000269|PubMed:14766310, ECO:0000269|PubMed:4867671, ECO:0000269|PubMed:4893578, ECO:0000269|PubMed:4920873, ECO:0000269|PubMed:4920894, ECO:0000269|PubMed:4934180, ECO:0000269|PubMed:8412694, ECO:0000269|PubMed:9312015}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GSDEADENYLATION-RXN|reaction.ecocyc.GSDEADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3053|gene.b3053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30870`
- `KEGG:ecj:JW3025;eco:b3053;ecoc:C3026_16680;`
- `GeneID:947552;`
- `GO:GO:0000287; GO:0000820; GO:0005524; GO:0005829; GO:0008882; GO:0047388; GO:0062132`
- `EC:2.7.7.42; 2.7.7.89`

## Notes

Bifunctional glutamine synthetase adenylyltransferase/adenylyl-removing enzyme (ATP:glutamine synthetase adenylyltransferase) (ATase) [Includes: Glutamine synthetase adenylyl-L-tyrosine phosphorylase (EC 2.7.7.89) (Adenylyl removase) (AR) (AT-N) (AT-N440) (P-I); Glutamine synthetase adenylyl transferase (EC 2.7.7.42) (Adenylyl transferase) (AT) (AT-C)]
