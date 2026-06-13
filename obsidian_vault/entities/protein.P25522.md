---
entity_id: "protein.P25522"
entity_type: "protein"
name: "mnmE"
source_database: "UniProt"
source_id: "P25522"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00379, ECO:0000269|PubMed:10601028}. Note=Partially associated with the inner membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mnmE thdF trmE b3706 JW3684"
---

# mnmE

`protein.P25522`

## Static

- Type: `protein`
- Source: `UniProt:P25522`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00379, ECO:0000269|PubMed:10601028}. Note=Partially associated with the inner membrane.

## Enriched Summary

FUNCTION: Exhibits a very high intrinsic GTPase hydrolysis rate. Involved in the addition of a carboxymethylaminomethyl (cmnm) group at the wobble position (U34) of certain tRNAs, forming tRNA-cmnm(5)s(2)U34. MnmE is required for wild-type 5-methylaminomethyl-2-thiouridine modification of tRNA . The additional modification of m5U stabilizes the U·G pairing at the wobble position and thus plays a role in decoding NNG codons . Together with MnmG, MnmE is involved in maintenance of the correct reading frame . MnmE also appeared to play a role in oxidation of thiophene and furan compounds and regulates glutamate-dependent acid resistance . MnmE is a GTP-binding protein that also exhibits GTPase activity, showing rapid GTP hydrolysis and low nucleotide affinity. The nucleotide binding and hydrolysis activities are localized within the central 17 kDa GTPase domain . The GTPase activity as well as the Cys451 residue in the C-terminal domain are required , but not sufficient for the wild-type tRNA modification function. Dimerization of the GTPase domain is potassium ion-dependent; subsequent GTP hydrolysis activity is dependent on dimerization . Low pH inhibits the GTP hydrolysis activity . Unlike other GTPases, MnmE does not appear to use an "arginine finger" for catalysis...

## Biological Role

Component of 5-carboxymethylaminomethyluridine-tRNA synthase GTPase subunit (complex.ecocyc.CPLX0-7608), 5-carboxymethylaminomethyluridine-tRNA synthase [multifunctional] (complex.ecocyc.CPLX0-7609).

## Annotation

FUNCTION: Exhibits a very high intrinsic GTPase hydrolysis rate. Involved in the addition of a carboxymethylaminomethyl (cmnm) group at the wobble position (U34) of certain tRNAs, forming tRNA-cmnm(5)s(2)U34.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7608|complex.ecocyc.CPLX0-7608]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7609|complex.ecocyc.CPLX0-7609]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3706|gene.b3706]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25522`
- `KEGG:ecj:JW3684;eco:b3706;ecoc:C3026_20095;`
- `GeneID:86861818;948222;`
- `GO:GO:0002098; GO:0002144; GO:0002926; GO:0003924; GO:0005525; GO:0005737; GO:0005829; GO:0005886; GO:0009268; GO:0019003; GO:0030488; GO:0030955; GO:0042802; GO:0042803; GO:0140018`
- `EC:3.6.-.-`

## Notes

tRNA modification GTPase MnmE (EC 3.6.-.-)
